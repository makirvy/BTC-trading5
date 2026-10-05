import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración inicial de la página (ancho completo y tema oscuro implícito)
st.set_page_config(
    page_title="Terminal BTCUSD | Live Monitor",
    page_icon="⚡",
    layout="wide"
)

# Estilos CSS personalizados para darle un toque más limpio y moderno (tipo dark mode pro)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        color: #8b949e;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 5px;
    }
    .metric-value {
        color: #f0f6fc;
        font-size: 24px;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.title("⚡ Terminal de Análisis — BTCUSD")
st.caption("Monitoreo en tiempo real sincronizado con MetaTrader 5 (IC Markets Demo)")

# Cargar datos locales
try:
    df = pd.read_csv("btc_ultimos_7_dias.csv")
    df['time'] = pd.to_datetime(df['time'])
except FileNotFoundError:
    st.error("⚠️️ No se encontró el archivo de datos ('btc_ultimos_7_dias.csv'). Ejecuta la extracción primero.")
    st.stop()

# Tarjetas de métricas personalizadas (KPIs) con HTML/CSS limpio
max_high = df['high'].max()
min_low = df['low'].min()
last_close = df['close'].iloc[-1]
total_vol = df['tick_volume'].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">TOTAL VELAS H1</div>
            <div class="metric-value">{len(df):,}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">MÁXIMO (7 DÍAS)</div>
            <div class="metric-value">${max_high:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">MÍNIMO (7 DÍAS)</div>
            <div class="metric-value">${min_low:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">ÚLTIMO CIERRE</div>
            <div class="metric-value">${last_close:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# Sección de gráficos y tabla principal
c_left, c_right = st.columns([1.6, 1])

with c_left:
    st.subheader("📈 Comportamiento del Precio (Cierre)")
    
    # Gráfica optimizada con estilo oscuro de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#161b22')
    
    ax.plot(df['time'], df['close'], color='#ff9900', linewidth=1.8, label='BTCUSD Close')
    
    ax.tick_params(colors='#8b949e', labelsize=10)
    ax.xaxis.label.set_color('#8b949e')
    ax.yaxis.label.set_color('#8b949e')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['top'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['right'].set_color('#30363d')
    
    ax.grid(True, linestyle='--', alpha=0.2, color='#8b949e')
    ax.legend(facecolor='#161b22', edgecolor='#30363d', labelcolor='white')
    
    st.pyplot(fig)

with c_right:
    st.subheader("📋 Registro Reciente")
    # Mostramos una tabla limpia con las columnas clave
    st.dataframe(
        df[['time', 'open', 'high', 'low', 'close', 'tick_volume']].tail(12).sort_values(by='time', ascending=False),
        height=320,
        use_container_width=True
    )