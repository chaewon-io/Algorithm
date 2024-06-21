def solution(n, lost, reserve):
    
    real_lost = [l for l in lost if l not in reserve]
    real_reserve = [r for r in reserve if r not in lost]
    
    count = 0
    
    for l in sorted(real_lost):
        if l-1 in real_reserve:
            real_reserve.remove(l-1)
            count += 1
        elif l+1 in real_reserve:
            real_reserve.remove(l+1)
            count += 1
        else:
            continue # 빌리지 못한 경우
    
    return n - len(real_lost) + count
