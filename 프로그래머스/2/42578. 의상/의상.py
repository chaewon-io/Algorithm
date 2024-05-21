def solution(clothes):
    clothes_dict = {}
    
    for _, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    
    combinations = 1
    for count in clothes_dict.values():
        combinations *= (count + 1)
    
    return combinations - 1