import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset de los últimos 7 días
df = pd.read_csv("btc_ultimos_7_dias.csv")
df['time'] = pd.to_datetime(df['time'])

# 2. Configurar la gráfica de evolución del precio de cierre (Close)
plt.figure(figsize=(12, 6))
plt.plot(df['time'], df['close'], label='Precio de Cierre (Close)', color='orange', linewidth=1.5)
plt.title('Análisis de Bitcoin (BTCUSD) - Últimos 7 Días (UTC)', fontsize=14, fontweight='bold')
plt.xlabel('Fecha y Hora (UTC)', fontsize=12)
plt.ylabel('Precio (USD)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# 3. Guardar la gráfica como imagen para el reporte visual
plt.savefig('btc_7dias_grafica.png', dpi=300)
print("Gráfica guardada exitosamente como 'btc_7dias_grafica.png'.")

# Mostrar la gráfica en pantalla
plt.show()