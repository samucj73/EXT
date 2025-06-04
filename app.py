import streamlit as st
from data_handler import fetch_latest_result
from streamlit_autorefresh import st_autorefresh
from analysis import analisar_estatisticas

st.set_page_config(page_title="Monitor XXXtreme", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎰 Monitor de Sorteios - XXXtreme Lightning Roulette</h1>", unsafe_allow_html=True)

# Autorefresh até 10 sorteios coletados
if "history" not in st.session_state:
    st.session_state.history = []
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = None
if len(st.session_state.history) < 10:
    st_autorefresh(interval=10_000, key="refresh")

# Coleta o resultado mais recente
result = fetch_latest_result()
if result and result["timestamp"] != st.session_state.last_seen_timestamp:
    st.session_state.history.insert(0, result)
    st.session_state.history = st.session_state.history[:50]
    st.session_state.last_seen_timestamp = result["timestamp"]

# Exibe resultados ao vivo
st.subheader("🎲 Últimos Números Sorteados:")
if st.session_state.history:
    for item in st.session_state.history[:10]:
        st.write(f"🎯 Número: {item['number']} | 🎨 Cor: {item['color']} | ⚡ Lucky: {item['lucky_numbers']} | 🕒 {item['timestamp']}")
else:
    st.info("⏳ Aguardando os primeiros resultados...")

st.markdown(f"<div style='text-align: center;'>📊 Sorteios coletados: <strong>{len(st.session_state.history)}</strong> / 50</div>", unsafe_allow_html=True)

# Botão de análise
if len(st.session_state.history) >= 10:
    st.subheader("📈 Pronto para análise!")
    if st.button("🔍 Analisar os 10 últimos sorteios"):
        analisar_estatisticas(st.session_state.history[:10])

# Botão de reinício
if st.button("♻️ Reiniciar Coleta"):
    st.session_state.history = []
    st.session_state.last_seen_timestamp = None
    st.experimental_rerun()

# Rodapé
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.9em;'>Desenvolvido por Kanō Systems © 2025</p>", unsafe_allow_html=True)
