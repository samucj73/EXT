import streamlit as st
from data_handler import fetch_latest_result, salvar_resultado_em_arquivo
from analysis import analisar_estatisticas
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Monitor XXXtreme", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎰 Monitor de Sorteios - XXXtreme Lightning Roulette</h1>", unsafe_allow_html=True)

# Parar auto refresh se 10 resultados já foram coletados
if "history" not in st.session_state:
    st.session_state.history = []
if "last_seen_timestamp" not in st.session_state:
    st.session_state.last_seen_timestamp = None
if "coletando" not in st.session_state:
    st.session_state.coletando = True

if len(st.session_state.history) < 10 and st.session_state.coletando:
    st_autorefresh(interval=10_000, key="refresh")

# 🔍 Busca o último resultado
result = fetch_latest_result()

if result and result["timestamp"] != st.session_state.last_seen_timestamp and st.session_state.coletando:
    st.session_state.history.insert(0, result)
    st.session_state.history = st.session_state.history[:10]
    st.session_state.last_seen_timestamp = result["timestamp"]

    # Salvar a cada 10
    if len(st.session_state.history) == 10:
        salvar_resultado_em_arquivo(st.session_state.history)
        st.session_state.coletando = False

# 🎯 Mostra números em tempo real
st.subheader("🎲 Números Sorteados ao Vivo:")
if st.session_state.history:
    for item in st.session_state.history:
        st.write(f"🎯 Número: {item['number']} | 🎨 Cor: {item.get('color', '-')}"
                 f" | ⚡ Lucky: {item['lucky_numbers']} | 🕒 {item['timestamp']}")
else:
    st.info("⏳ Aguardando os primeiros números...")

st.markdown(f"📊 Números coletados: **{len(st.session_state.history)}** / 10")

# 🔁 Botão para reiniciar
if not st.session_state.coletando:
    if st.button("🔁 Reiniciar Coleta"):
        st.session_state.history = []
        st.session_state.coletando = True

# 📈 Análise quando atingir 10
if len(st.session_state.history) == 10:
    st.subheader("📈 Pronto para análise!")
    if st.button("🔍 Analisar os 10 últimos sorteios"):
        stats = analisar_estatisticas(st.session_state.history)

        st.markdown("### 🎯 Frequência dos Números (Top 10)", unsafe_allow_html=True)
        for n, f in stats["frequencia"][:10]:
            st.write(f"➡️ Número {n} saiu **{f}x**")

        st.markdown("### ⚡ Lucky Numbers Mais Frequentes", unsafe_allow_html=True)
        for n, f in stats["lucky_frequencia"]:
            st.write(f"🌟 Lucky {n}: apareceu **{f}x**")

        st.markdown("### 🎨 Cores", unsafe_allow_html=True)
        st.write(f"🔴 Vermelhos: {stats['vermelho']} | ⚫ Pretos: {stats['preto']}")

        st.markdown("### 🔢 Pares / Ímpares", unsafe_allow_html=True)
        st.write(f"🔷 Pares: {stats['pares']} | 🔶 Ímpares: {stats['impares']}")

        st.markdown("### 🧭 Baixos / Altos", unsafe_allow_html=True)
        st.write(f"⬇️ Baixos (1-18): {stats['baixos']} | ⬆️ Altos (19-36): {stats['altos']}")

        st.markdown("### 🏛️ Colunas", unsafe_allow_html=True)
        for col, qnt in stats["colunas"].items():
            st.write(f"📊 Coluna {col}: {qnt} números")

        st.markdown("### 🧱 Linhas", unsafe_allow_html=True)
        for lin, qnt in stats["linhas"].items():
            st.write(f"📈 Linha {lin}: {qnt} números")

        st.markdown("### 🔮 Previsão Refinada dos Próximos 10 Números", unsafe_allow_html=True)
        st.success("🎯 Números Prováveis:")
        st.markdown(
            "<div style='font-size: 28px; text-align: center; color: darkblue;'>"
            + " | ".join(str(n) for n in stats["previsao"]) +
            "</div>",
            unsafe_allow_html=True
        )

# 🔻 Rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 13px; color: gray;'>"
    "🔧 Desenvolvido com inteligência estatística • XXXtreme Monitor"
    "</div>",
    unsafe_allow_html=True
)
