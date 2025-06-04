from analysis import analisar_estatisticas

# Dentro do botão:
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
