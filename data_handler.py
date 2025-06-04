import requests

API_URL = "https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Mapeamento auxiliar
def get_line(number):
    if number == 0:
        return None
    return ((number - 1) % 3) + 1  # 1: primeira, 2: segunda, 3: terceira

def get_column(number):
    if number == 0:
        return None
    return ((number - 1) // 3) + 1  # coluna de 1 a 12

def is_low(number):
    return number != 0 and number <= 18

def is_high(number):
    return number >= 19

def fetch_latest_result():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            game_data = data.get("data", {})
            result = game_data.get("result", {})
            outcome = result.get("outcome", {})
            lucky_list = result.get("luckyNumbersList", [])

            number = outcome.get("number")
            timestamp = game_data.get("startedAt")
            lucky_numbers = [item["number"] for item in lucky_list]
            color = outcome.get("color", "Unknown")
            parity = outcome.get("type", "Unknown")
            line = get_line(number)
            column = get_column(number)
            low_high = "Low" if is_low(number) else "High" if is_high(number) else "Zero"

            return {
                "number": number,
                "timestamp": timestamp,
                "lucky_numbers": lucky_numbers,
                "color": color,
                "parity": parity,
                "line": line,
                "column": column,
                "low_high": low_high
            }
    except Exception as e:
        return None
