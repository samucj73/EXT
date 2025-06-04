import streamlit as st
import time
from data_handler import fetch_latest_result, update_history

st.set_page_config(page_title="XXXtreme Monitor", layout="centered")
st.title("🎰 XXXtreme Lightning Roulette - Monitor Automático")

# Inicializa estado
if "history" not in st.session_state:
    st.session_state.history = []
if "last_check" not in st.session_state:
    st.session_state.last_check = time.time()

# ⚙️ Monitoramento automático (verifica a cada 15 segundos)
if time.time() - st.session_state.last_check > 15:
    result = fetch_latest_result()
    st.session_state.history = update_history(st.session_state.history, result)
    st.session_state.last_check = time.time()

# 🔢 Mostra progresso
st.markdown(f"🔄 Números monitorados: **{len(st.session_state.history)}** / 50")

# 🧠 Análise ao clicar
if st.button("📊 Analisar Números Coletados"):
    if len(st.session_state.history) < 10:
        st.warning("Aguardando mais números serem monitorados para uma análise significativa.")
    else:
        st.success("Analisando os dados coletados...")
        nums = [item["number"] for item in st.session_state.history]
        mais_frequentes = {n: nums.count(n) for n in set(nums)}
        ordenado = sorted(mais_frequentes.items(), key=lambda x: x[1], reverse=True)

        st.subheader("🎯 Números mais frequentes")
        for n, freq in ordenado[:10]:
            st.write(f"Número {n}: {freq}x")

# 🧾 Histórico recente
st.subheader("📜 Últimos Resultados Monitorados")
for item in st.session_state.history[:10]:
    st.write(f"🎲 {item['number']} | ⚡ {item['lucky_numbers']} | 🕒 {item['timestamp']}")
