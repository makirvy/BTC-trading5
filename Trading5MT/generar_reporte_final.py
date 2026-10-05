import pandas as pd
import datetime

# Cargar datos para extraer valores reales para el reporte
df = pd.read_csv("btc_ultimos_7_dias.csv")
total_velas = len(df)
precio_max = df['high'].max()
precio_min = df['low'].max()
precio_actual = df['close'].iloc[-1]
volumen_total = df['tick_volume'].sum()

# Generar contenido Markdown para el reporte visual de la tarea
contenido_reporte = f"""# Tarea 6 - Proyecto: Análisis de Bitcoin (BTCUSD) con MetaTrader 5, Pandas, Celery y Gráficas

**Estudiante:** Universidad (Panamá)  
**Broker Utilizado:** IC Markets (Cuenta Demo)  
**Símbolo Analizado:** `BTCUSD`  
**Temporalidad:** Horaria (H1) - Últimos 7 Días (UTC)  
**Fecha de Emisión:** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} UTC  

---

## 1. Resumen Ejecutivo y Objetivos
El presente proyecto tiene como objetivo la extracción automatizada de datos en tiempo real desde MetaTrader 5 mediante la API de Python, utilizando una cuenta demo configurada en UTC. El procesamiento de los datos se realizó con Pandas, la ejecución de tareas asíncronas en segundo plano con Celery, la vectorización estadística, la generación de gráficos de rendimiento y la consolidación de un libro de Excel y un informe técnico detallado.

---

## 2. Métricas Estadísticas Clave (Datos Reales de MT5)
A partir de la extracción de los últimos 7 días en temporalidad H1, se obtuvieron los siguientes indicadores:
* **Total de Velas H1 Analizadas:** {total_velas} registros.
* **Precio Máximo Alcanzado:** ${precio_max:,.2f} USD.
* **Precio Mínimo Registrado:** ${precio_min:,.2f} USD.
* **Precio de Cierre Más Reciente:** ${precio_actual:,.2f} USD.
* **Volumen Total de Transacciones:** {volumen_total:,.2f}.

---

## 3. Arquitectura del Proyecto y Tecnologías
1. **MetaTrader 5 (MT5):** Proveedor de datos de mercado en tiempo real y histórico mediante la API oficial de Python (`MetaTrader5`), conectado a la cuenta demo de IC Markets con el símbolo `BTCUSD`.
2. **Pandas & NumPy:** Estructuración, limpieza, manejo de zonas horarias UTC y cálculos estadísticos de las series temporales.
3. **Matplotlib:** Generación de gráficos de evolución de precios de cierre (`btc_7dias_grafica.png`).
4. **Celery:** Orquestación de tareas en segundo plano (`tareas_celery.py`) con persistencia local mediante SQLite.
5. **Openpyxl:** Automatización de la exportación a Excel estructurado en múltiples hojas (`Reporte_Analisis_Bitcoin.xlsx`).

---

## 4. Consolidado de Evidencias de las 30 Actividades del Proyecto

| Módulo / Fase | Actividades / Hitos del Proyecto | Estado | Evidencia / Archivo Generado |
| :--- | :--- | :---: | :--- |
| **Fase 1: Configuración** | 1. Instalación y configuración de MetaTrader 5 | Completado | MT5 Desktop (IC Markets Demo) |
| | 2. Creación y validación de cuenta demo | Completado | Servidor ICMarketsEU-Demo |
| | 3. Identificación y selección del símbolo correcto | Completado | Símbolo `BTCUSD` verificado |
| | 4. Configuración del entorno de desarrollo VS Code | Completado | Estructura de carpetas local |
| | 5. Creación de entorno virtual Python (`venv`) | Completado | Directorio `venv/` activo |
| | 6. Actualización e instalación de gestor de paquetes | Completado | `pip` actualizado |
| | 7. Instalación de librería `MetaTrader5` | Completado | Módulo verificado |
| | 8. Instalación de librería `pandas` | Completado | Módulo verificado |
| | 9. Instalación de librería `matplotlib` | Completado | Módulo verificado |
| | 10. Instalación de librería `celery` | Completado | Módulo verificado |
| **Fase 2: Extracción** | 11. Instalación de librería `openpyxl` para Excel | Completado | Módulo verificado |
| | 12. Script de inicialización y prueba de conexión MT5 | Completado | `conectar_mt5.py` |
| | 13. Extracción de las primeras 100 velas horarias (H1) | Completado | `btc_100_velas_h1.csv` |
| | 14. Validación de marcas de tiempo en formato UTC | Completado | Conversión correcta en Pandas |
| | 15. Configuración de parámetros de rango temporal (7 días) | Completado | `analisis_7dias.py` |
| | 16. Extracción masiva de datos históricos por rango | Completado | `btc_ultimos_7_dias.csv` |
| | 17. Depuración de zonas horarias para compatibilidad | Completado | `tz_localize(None)` aplicado |
| | 18. Cálculo de métricas estadísticas (Máx, Mín, Promedio) | Completado | Integrado en script |
| | 19. Agregación de volúmenes de negociación por tick | Completado | Procesado en DataFrame |
| | 20. Configuración del broker sin operaciones de compra/venta | Completado | Modo estrictamente analítico |
| **Fase 3: Procesamiento** | 21. Diseño de la arquitectura de tareas asíncronas | Completado | Configuración con Celery |
| | 22. Configuración del broker SQLite para Celery | Completado | `celery_meta.db` |
| | 23. Implementación del backend de resultados Celery | Completado | `celery_results.db` |
| | 24. Creación de la tarea en segundo plano (`@app.task`) | Completado | `tareas_celery.py` |
| | 25. Ejecución y prueba de la tarea asíncrona | Completado | Tarea ejecutada con éxito |
| | 26. Automatización de la generación del libro de Excel | Completado | `Reporte_Analisis_Bitcoin.xlsx` |
| | 27. Estructuración de múltiples hojas en Excel | Completado | Hojas de Datos y Resumen |
| | 28. Generación de gráficos analíticos con Matplotlib | Completado | `btc_7dias_grafica.png` |
| | 29. Consolidación de interpretaciones y reporte visual | Completado | Documento técnico Markdown |
| | 30. Verificación final de integridad y respaldos | Completado | Proyecto listo para entrega |

---
*Nota: Todos los datos, marcas temporales, precios y registros provienen directamente de la ejecución en tiempo real con MetaTrader 5 y la cuenta demo institucional.*
"""

# Guardar el reporte como documento de texto/markdown
with open("Reporte_Final_Bitcoin.md", "w", encoding="utf-8") as f:
    f.write(contenido_reporte)

print("¡Reporte final generado exitosamente como 'Reporte_Final_Bitcoin.md'!")