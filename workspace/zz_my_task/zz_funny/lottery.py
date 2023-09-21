import random

def generate_lotto_numbers():
    return sorted(random.sample(range(1, 46), 6))

print("추천 로또 번호:", generate_lotto_numbers())