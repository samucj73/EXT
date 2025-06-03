from collections import Counter

def get_frequency(history):
    numbers = [entry["number"] for entry in history]
    return Counter(numbers)

def get_hot_and_cold(freq_counter, top_n=5):
    most_common = freq_counter.most_common()
    hot = most_common[:top_n]
    cold = most_common[-top_n:]
    return hot, cold