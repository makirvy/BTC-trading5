import MetaTrader5 as mt5
import pandas as pd

# 1. Inicializar la conexión con MetaTrader 5
if not mt5.initialize():
    print(f"initialize() falló, error código = {mt5.last_error()}")
    mt5.shutdown()
else:
    print("¡Conexión con MetaTrader 5 exitosa!")

    # 2. Configurar el símbolo exacto que encontramos
    symbol = "BTCUSD"

    # 3. Asegurar que el símbolo esté seleccionado en la observación de mercado
    selected = mt5.symbol_select(symbol, True)
    if not selected:
        print(f"Falló al seleccionar {symbol}, error = {mt5.last_error()}")
    else:
        # 4. Obtener las 100 velas horarias (TIMEFRAME_H1)
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 100)
        
        if rates is not None and len(rates) > 0:
            # Convertir a DataFrame de Pandas
            df = pd.DataFrame(rates)
            # Convertir la hora de formato timestamp a UTC legible
            df['time'] = pd.to_datetime(df['time'], unit='s')
            
            print(f"\nPrimeras 5 velas horarias para {symbol} (en UTC):")
            print(df[['time', 'open', 'high', 'low', 'close', 'tick_volume']].head())
            
            # Guardar un respaldo en CSV para verificar
            df.to_csv("btc_100_velas_h1.csv", index=False)
            print("\nDatos guardados exitosamente en 'btc_100_velas_h1.csv'.")
        else:
            print(f"No se pudieron obtener datos para {symbol}.")

    # 5. Cerrar la conexión
    mt5.shutdown()