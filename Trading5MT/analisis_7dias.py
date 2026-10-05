import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timezone, timedelta

# 1. Inicializar MetaTrader 5
if not mt5.initialize():
    print(f"Error al inicializar MT5: {mt5.last_error()}")
else:
    symbol = "BTCUSD"
    mt5.symbol_select(symbol, True)

    # 2. Definir rango de los últimos 7 días en UTC
    utc_to = datetime.now(timezone.utc)
    utc_from = utc_to - timedelta(days=7)

    # Obtener tasas (copiar barras por rango de fechas en H1)
    rates = mt5.copy_rates_range(symbol, mt5.TIMEFRAME_H1, utc_from, utc_to)

    if rates is not None and len(rates) > 0:
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s', utc=True)
        
        print(f"Total de registros obtenidos para los últimos 7 días: {len(df)}")
        print(df.head())

        # Guardar dataset de 7 días
        df.to_csv("btc_ultimos_7_dias.csv", index=False)
        print("Dataset de 7 días guardado en 'btc_ultimos_7_dias.csv'.")
    else:
        print("No se pudieron obtener los datos por rango de fecha.")

    mt5.shutdown()