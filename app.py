import streamlit as st
import threading
import time
from data_handler import fetch_latest_result, update_history
from analyzer import get_frequency, get_hot_and_cold
from predictor import predict_next

st.set_page_config(page_title="XXXtreme Roulette Monitor", layout="wide")

# Inicializa histórico
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🎰 Monitor de Números - XXXtreme Lightning Roulette")

def background_updater():
    while True:
        latest = fetch_latest_result()
        if latest:
            st.session_state.history = update_history(st.session_state.history, latest)
        time.sleep(30)  # Atualiza a cada 30 segundos

# Inicia o monitoramento em background (apenas uma vez)
if "thread_started" not in st.session_state:
    thread = threading.Thread(target=background_updater, daemon=True)
    thread.start()
    st.session_state.thread_started = True

st.subheader("📉 Números Monitorados (Últimos 50)")
st.write([h["number"] for h in st.session_state.history])

if st.button("📊 Analisar Dados Coletados"):
    freq = get_frequency(st.session_state.history)
    hot, cold = get_hot_and_cold(freq)
    prediction = predict_next(freq)

    st.subheader("🔥 Números Quentes")
    st.write(hot)

    st.subheader("❄️ Números Frios")
    st.write(cold)

    st.subheader("🔮 Previsão do Próximo Número")
    st.write(prediction)