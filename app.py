import streamlit as st
import time
from data_handler import fetch_latest_result

st.set_page_config(page_title="Monitor XXXtreme", layout="centered")
st.title("🎰 Monitor de Sorteios - XXXtreme Lightning Roulette")

if "history" not in st.session_state:
    st.session_state.history = []
if "last_check" not in st.session_state:
    st.session_state.last_check = 0
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = None

# ⏱ Atualiza a cada 10 segundos
if time.time() - st.session_state.last_check > 10:
    result = fetch_latest_result()
    st.session_state.last_check = time.time()

    if result and result["timestamp"] != st.session_state.last_seen_timestamp:
        st.session_state.history.insert(0, result)
        st.session_state.history = st.session_state.history[:50]
        st.session_state.last_seen_timestamp = result["timestamp"]

# 🔢 Mostra os números sendo sorteados (estilo “bot”)
st.subheader("🎲 Números Sorteados ao Vivo:")
if st.session_state.history:
    for item in st.session_state.history[:10]:  # mostra os 10 mais recentes
        st.write(f"🎯 Número: {item['number']} | ⚡ Lucky: {item['lucky_numbers']} | 🕒 {item['timestamp']}")
else:
    st.info("Aguardando os primeiros números serem sorteados...")

st.markdown(f"🔄 Total de números capturados: **{len(st.session_state.history)}** / 50")

# 🔘 Botão de análise só aparece se houver 50 números
if len(st.session_state.history) >= 50:
    st.subheader("📊 Pronto para análise!")
    if st.button("🔍 Analisar os 50 últimos sorteios"):
        numeros = [item["number"] for item in st.session_state.history]
        freq = {n: numeros.count(n) for n in set(numeros)}
        ordenado = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        st.write("🎯 **Top 10 Números Mais Frequentes**:")
        for n, f in ordenado[:10]:
            st.write(f"➡️ Número {n} saiu {f} vezes")

        # Lucky numbers análise
        lucky_total = []
        for item in st.session_state.history:
            lucky_total.extend(item["lucky_numbers"])
        lucky_freq = {n: lucky_total.count(n) for n in set(lucky_total)}
        lucky_ordenado = sorted(lucky_freq.items(), key=lambda x: x[1], reverse=True)

        st.write("⚡ **Lucky Numbers Mais Frequentes**:")
        for n, f in lucky_ordenado[:5]:
            st.write(f"🌟 Lucky {n}: apareceu {f} vezes")
