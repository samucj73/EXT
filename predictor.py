import random

def predict_next(freq_counter):
    hot_numbers = [n for n, _ in freq_counter.most_common(10)]
    return random.choice(hot_numbers) if hot_numbers else None