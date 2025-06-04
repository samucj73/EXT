import streamlit as st
from data_handler import fetch_latest_result, update_history

st.set_page_config(page_title="XXXtreme Lightning Monitor", layout="centered")
st.title("⚡ XXXtreme Lightning Roulette Monitor")

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("Clique no botão abaixo para buscar e analisar o próximo número sorteado:")

if st.button("🔍 Analisar Números"):
    latest = fetch_latest_result()
    st.session_state.history = update_history(st.session_state.history, latest)
    if latest:
        st.success(f"Número {latest['number']} capturado com sucesso!")
    else:
        st.warning("Nenhum novo número encontrado.")

st.subheader("📊 Últimos Números Monitorados")

if st.session_state.history:
    for item in st.session_state.history:
        st.write(f"""
        🎯 **Número**: {item['number']}  
        ⚡ **Multiplicadores**: {item['lucky_numbers']}  
        🕒 **Horário**: {item['timestamp']}
        """)
else:
    st.info("Nenhum número foi capturado ainda.")
