from collections import Counter, defaultdict

def get_color(number):
    red_numbers = {
        1, 3, 5, 7, 9, 12, 14, 16, 18,
        19, 21, 23, 25, 27, 30, 32, 34, 36
    }
    if number == 0:
        return "verde"
    return "vermelho" if number in red_numbers else "preto"

def get_coluna(n):
    return (n - 1) % 3 + 1 if n != 0 else None

def get_linha(n):
    return ((n - 1) // 3) + 1 if n != 0 else None

def analisar_estatisticas(history):
    numeros = [item["number"] for item in history]
    lucky_all = [n for item in history for n in item["lucky_numbers"]]

    freq = Counter(numeros)
    lucky_freq = Counter(lucky_all)
    cor_freq = Counter(get_color(n) for n in numeros)
    pares = sum(1 for n in numeros if n != 0 and n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 == 1)
    baixos = sum(1 for n in numeros if 1 <= n <= 18)
    altos = sum(1 for n in numeros if 19 <= n <= 36)
    colunas = Counter(get_coluna(n) for n in numeros if n != 0)
    linhas = Counter(get_linha(n) for n in numeros if n != 0)

    # 📊 Previsão refinada
    scores = defaultdict(float)

    for n in range(37):
        if n == 0:
            continue

        scores[n] += freq[n] * 2  # frequência normal (peso 2)
        scores[n] += lucky_freq[n] * 1.5  # frequência lucky (peso 1.5)

        # paridade
        if n % 2 == 0:
            scores[n] += pares / max(1, len(numeros))
        else:
            scores[n] += impares / max(1, len(numeros))

        # altura
        if 1 <= n <= 18:
            scores[n] += baixos / max(1, len(numeros))
        elif 19 <= n <= 36:
            scores[n] += altos / max(1, len(numeros))

        # colunas
        col = get_coluna(n)
        if col:
            scores[n] += colunas[col] / max(1, len(numeros))

        # linhas
        linha = get_linha(n)
        if linha:
            scores[n] += linhas[linha] / max(1, len(numeros))

        # cor
        cor = get_color(n)
        if cor in cor_freq:
            scores[n] += cor_freq[cor] / max(1, len(numeros))

    previsao = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_10 = [n for n, _ in previsao[:10]]

    return {
        "frequencia": freq.most_common(),
        "lucky_frequencia": lucky_freq.most_common(5),
        "vermelho": cor_freq.get("vermelho", 0),
        "preto": cor_freq.get("preto", 0),
        "pares": pares,
        "impares": impares,
        "colunas": dict(colunas),
        "linhas": dict(linhas),
        "baixos": baixos,
        "altos": altos,
        "previsao": top_10
    }
