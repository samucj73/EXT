import requests
from datetime import datetime

API_URL = "https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Histórico para evitar duplicatas
seen_ids = set()

def fetch_latest_result():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            game_id = data.get("id")
            if game_id and game_id not in seen_ids:
                seen_ids.add(game_id)
                number = data["data"]["result"]["outcome"]["number"]
                lucky = data["data"]["result"]["luckyNumbersList"]
                return {
                    "id": game_id,
                    "number": number,
                    "lucky_numbers": lucky,
                    "timestamp": data["data"]["startedAt"]
                }
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")
    return None

def update_history(history, new_result, limit=50):
    if new_result and (not history or history[0]["number"] != new_result["number"]):
        history.insert(0, {
            "number": new_result["number"],
            "timestamp": datetime.now().isoformat(),
            "lucky_numbers": new_result["lucky_numbers"]
        })
        return history[:limit]
    return history
