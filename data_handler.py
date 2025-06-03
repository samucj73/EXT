import requests
from datetime import datetime

API_URL = "https://xxxtremelightningrouletteapi.p.rapidapi.com/latest-outcome"
HEADERS = {
    "x-rapidapi-host": "xxxtremelightningrouletteapi.p.rapidapi.com",
    "x-rapidapi-key": "61871c5fc9mshfc11eedc4edd0eap1d3db2jsn856cbb79b4af"
}

def fetch_latest_result():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("outcome")
    except Exception:
        return None
    return None

def update_history(history, new_result, limit=50):
    if new_result and (not history or history[0]["number"] != new_result):
        history.insert(0, {
            "number": new_result,
            "timestamp": datetime.now().isoformat()
        })
        return history[:limit]
    return history