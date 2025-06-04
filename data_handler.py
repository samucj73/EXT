import requests
from datetime import datetime

API_URL = "https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

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

            if number is not None:
                return {
                    "number": number,
                    "timestamp": timestamp,
                    "lucky_numbers": lucky_numbers
                }
        else:
            print(f"Erro HTTP: {response.status_code}")
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
    return None

def update_history(history, new_result, limit=50):
    if new_result and (not history or history[0]["timestamp"] != new_result["timestamp"]):
        history.insert(0, new_result)
        return history[:limit]
    return history
