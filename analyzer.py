from collections import Counter

# Tabelas auxiliares da roleta europeia (0 a 36)
RED_NUMBERS = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
BLACK_NUMBERS = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

def get_frequency(history):
    numbers = [entry["number"] for entry in history]
    return Counter(numbers)

def get_hot_and_cold(freq_counter, top_n=5):
    most_common = freq_counter.most_common()
    hot = most_common[:top_n]
    cold = most_common[-top_n:]
    return hot, cold

def count_red_black(numbers):
    red = sum(1 for n in numbers if n in RED_NUMBERS)
    black = sum(1 for n in numbers if n in BLACK_NUMBERS)
    zero = numbers.count(0)
    return {"red": red, "black": black, "zero": zero}

def count_even_odd(numbers):
    even = sum(1 for n in numbers if n != 0 and n % 2 == 0)
    odd = sum(1 for n in numbers if n % 2 == 1)
    return {"even": even, "odd": odd}

def count_high_low(numbers):
    low = sum(1 for n in numbers if 1 <= n <= 18)
    high = sum(1 for n in numbers if 19 <= n <= 36)
    return {"low": low, "high": high}

def count_columns(numbers):
    col1 = sum(1 for n in numbers if n != 0 and (n - 1) % 3 == 0)
    col2 = sum(1 for n in numbers if n != 0 and (n - 2) % 3 == 0)
    col3 = sum(1 for n in numbers if n != 0 and n % 3 == 0)
    return {"col1": col1, "col2": col2, "col3": col3}

def count_dozen(numbers):
    d1 = sum(1 for n in numbers if 1 <= n <= 12)
    d2 = sum(1 for n in numbers if 13 <= n <= 24)
    d3 = sum(1 for n in numbers if 25 <= n <= 36)
    return {"1st Dozen": d1, "2nd Dozen": d2, "3rd Dozen": d3}
