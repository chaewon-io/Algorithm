from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_combinations(numbers):
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            num_set.add(num)
    return num_set

def count_primes(num_set):
    prime_count = 0
    for num in num_set:
        if is_prime(num):
            prime_count += 1
    return prime_count

def solution(numbers):
    num_set = generate_combinations(numbers)
    return count_primes(num_set)

