import streamlit as st
import time
from data_handler import fetch_latest_result
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Monitor XXXtreme", layout="centered")
st.title("🎰 Monitor de Sorteios - XXXtreme Lightning Roulette")

# 🔄 Atualiza automaticamente a cada 10 segundos
st_autorefresh(interval=10_000, key="refresh")

# Inicializa estados
if "history" not in st.session_state:
    st.session_state.history = []
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = None

# 🔍 Busca o último resultado
result = fetch_latest_result()

if result and result["timestamp"] != st.session_state.last_seen_timestamp:
    st.session_state.history.insert(0, result)
    st.session_state.history = st.session_state.history[:50]
    st.session_state.last_seen_timestamp = result["timestamp"]

# 🎯 Mostra números em tempo real
st.subheader("🎲 Números Sorteados ao Vivo:")
if st.session_state.history:
    for item in st.session_state.history[:10]:
        st.write(f"🎯 Número: {item['number']} | ⚡ Lucky: {item['lucky_numbers']} | 🕒 {item['timestamp']}")
else:
    st.info("⏳ Aguardando os primeiros números...")

st.markdown(f"📊 Números coletados: **{len(st.session_state.history)}** / 50")

# Botão de análise aparece ao atingir 50
if len(st.session_state.history) >= 50:
    st.subheader("📈 Pronto para análise!")
    if st.button("🔍 Analisar os 50 últimos sorteios"):
        numeros = [item["number"] for item in st.session_state.history]
        freq = {n: numeros.count(n) for n in set(numeros)}
        ordenado = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        st.write("🎯 **Top 10 Números Mais Frequentes**:")
        for n, f in ordenado[:10]:
            st.write(f"➡️ Número {n} saiu {f} vezes")

        lucky_total = []
        for item in st.session_state.history:
            lucky_total.extend(item["lucky_numbers"])
        lucky_freq = {n: lucky_total.count(n) for n in set(lucky_total)}
        lucky_ordenado = sorted(lucky_freq.items(), key=lambda x: x[1], reverse=True)

        st.write("⚡ **Lucky Numbers Mais Frequentes**:")
        for n, f in lucky_ordenado[:5]:
            st.write(f"🌟 Lucky {n}: apareceu {f} vezes")
