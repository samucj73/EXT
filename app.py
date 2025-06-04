import streamlit as st
from data_handler import fetch_latest_result
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Monitor XXXtreme", layout="centered")

MAX_RESULTADOS = 10

# Inicializa estados
if "history" not in st.session_state:
    st.session_state.history = []
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = None
if "monitorando" not in st.session_state:
    st.session_state.monitorando = True

# 🔄 Auto refresh a cada 10s enquanto não atingiu o máximo
if st.session_state.monitorando and len(st.session_state.history) < MAX_RESULTADOS:
    st_autorefresh(interval=10_000, key="refresh")

# 🧠 Coleta dados da API
result = fetch_latest_result()
if result and result["timestamp"] != st.session_state.last_seen_timestamp:
    st.session_state.history.insert(0, result)
    st.session_state.history = st.session_state.history[:MAX_RESULTADOS]
    st.session_state.last_seen_timestamp = result["timestamp"]

# 🎰 Título centralizado
st.markdown("<h1 style='text-align: center;'>🎰 Monitor de Sorteios - XXXtreme Lightning Roulette</h1>", unsafe_allow_html=True)

# 🎲 Números Sorteados
st.markdown("<h3 style='text-align: center;'>🎲 Números Sorteados ao Vivo:</h3>", unsafe_allow_html=True)
if st.session_state.history:
    for item in st.session_state.history:
        st.write(f"🎯 Número: {item['number']} | ⚡ Lucky: {item['lucky_numbers']} | 🕒 {item['timestamp']}")
else:
    st.info("⏳ Aguardando os primeiros números...")

st.markdown(f"<p style='text-align: center;'>📊 Números coletados: <strong>{len(st.session_state.history)}</strong> / {MAX_RESULTADOS}</p>", unsafe_allow_html=True)

# 📈 Análise
if len(st.session_state.history) >= MAX_RESULTADOS:
    st.success("✅ Coleta concluída! Pronto para análise.")
    
    if st.button("🔍 Analisar os últimos sorteios"):
        numeros = [item["number"] for item in st.session_state.history]
        freq = {n: numeros.count(n) for n in set(numeros)}
        ordenado = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        st.markdown("<h4 style='text-align: center;'>🎯 Top Números Mais Frequentes:</h4>", unsafe_allow_html=True)
        for n, f in ordenado[:10]:
            st.write(f"➡️ Número {n}: {f} vezes")

        lucky_total = []
        for item in st.session_state.history:
            lucky_total.extend(item["lucky_numbers"])
        lucky_freq = {n: lucky_total.count(n) for n in set(lucky_total)}
        lucky_ordenado = sorted(lucky_freq.items(), key=lambda x: x[1], reverse=True)

        st.markdown("<h4 style='text-align: center;'>⚡ Lucky Numbers Mais Frequentes:</h4>", unsafe_allow_html=True)
        for n, f in lucky_ordenado[:5]:
            st.write(f"🌟 Lucky {n}: {f} vezes")

    if st.button("🔄 Reiniciar Monitoramento"):
        st.session_state.history = []
        st.session_state.last_seen_timestamp = None
        st.session_state.monitorando = True
        st.experimental_rerun()
else:
    st.info("🛰️ Monitorando...")

# ✅ Rodapé padrão centralizado
st.markdown("---", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: gray;'>Desenvolvido por <strong>Seu Nome</strong> • © 2025 XXXtreme Analyzer</p>",
    unsafe_allow_html=True
)
