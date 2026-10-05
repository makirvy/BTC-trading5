import os
import pandas as pd
from celery import Celery
import MetaTrader5 as mt5
from datetime import datetime, timezone, timedelta

# Configurar Celery con un broker local (usamos SQLite o RPC si no hay Redis instalado, o localhost)
app = Celery('tareas_bitcoin', broker='sqla+sqlite:///celery_meta.db', backend='db+sqlite:///celery_results.db')

@app.task
def generar_excel_y_reporte_background():
    """Tarea en segundo plano para procesar datos, generar Excel y consolidar la tarea."""
    print("[Celery] Iniciando procesamiento en segundo plano...")
    
    if not mt5.initialize():
        return "Error al conectar con MT5 en segundo plano"
    
    symbol = "BTCUSD"
    mt5.symbol_select(symbol, True)
    
    utc_to = datetime.now(timezone.utc)
    utc_from = utc_to - timedelta(days=7)
    rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H1, utc_from, utc_to)
    mt5.shutdown()
    
    if rates is None or len(rates) == 0:
        return "No se pudieron obtener datos para el Excel."
        
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s', utc=True)
    
    # CORRECCIÓN: Quitar la zona horaria para que Excel acepte el formato de fecha
    df['time'] = df['time'].dt.tz_localize(None)
    
    # Calcular estadísticas básicas para las actividades
    resumen = {
        "Total Velas H1": len(df),
        "Precio Máximo": float(df['high'].max()),
        "Precio Mínimo": float(df['low'].min()),
        "Precio Promedio Cierre": float(df['close'].mean()),
        "Volumen Total": float(df['tick_volume'].sum())
    }
    
    df_resumen = pd.DataFrame([resumen])
    
    # Generar Libro de Excel con openpyxl
    excel_file = "Reporte_Analisis_Bitcoin.xlsx"
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Datos_Historicos_7Dias', index=False)
        df_resumen.to_excel(writer, sheet_name='Resumen_Estadistico', index=False)
        
    print(f"[Celery] Archivo Excel generado con éxito: {excel_file}")
    return f"Procesamiento completado. Archivo {excel_file} creado."

if __name__ == '__main__':
    # Prueba local de ejecución
    resultado = generar_excel_y_reporte_background()
    print(resultado)