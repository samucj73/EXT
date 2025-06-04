from collections import Counter
import streamlit as st

def analisar_estatisticas(history):
    numeros = [item["number"] for item in history]
    cores = [item["color"].lower() for item in history]

    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = len(numeros) - pares
    baixos = sum(1 for n in numeros if 1 <= n <= 18)
    altos = sum(1 for n in numeros if 19 <= n <= 36)

    vermelhos = cores.count("red")
    pretos = cores.count("black")

    colunas = [((n - 1) % 3 + 1) for n in numeros if n != 0]
    duzias = [((n - 1) // 12 + 1) for n in numeros if n != 0]

    st.write("🎯 **Top 5 Números Mais Frequentes:**")
    for n, freq in Counter(numeros).most_common(5):
        st.write(f"➡️ Número {n}: {freq} vezes")

    st.write("🥶 **Top 5 Números Menos Frequentes:**")
    for n, freq in Counter(numeros).most_common()[-5:]:
        st.write(f"🔹 Número {n}: {freq} vezes")

    st.write("🔴⚫ **Cores:**")
    st.write(f"🔴 Vermelhos: {vermelhos} | ⚫ Pretos: {pretos}")

    st.write("🧮 **Pares e Ímpares:**")
    st.write(f"➕ Pares: {pares} | ➖ Ímpares: {impares}")

    st.write("📈 **Altos e Baixos:**")
    st.write(f"🔽 Baixos (1-18): {baixos} | 🔼 Altos (19-36): {altos}")

    st.write("📊 **Colunas (1 a 3):**")
    for i in range(1, 4):
        st.write(f"📌 Coluna {i}: {colunas.count(i)}x")

    st.write("🧩 **Dúzias (1ª a 3ª):**")
    for i in range(1, 4):
        st.write(f"📌 Dúzia {i}: {duzias.count(i)}x")
