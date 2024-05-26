from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

def solution(numbers):
    numbers_str = list(map(str, numbers))
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))
    largest_number = ''.join(sorted_numbers)
    return largest_number if largest_number[0] != '0' else '0'
