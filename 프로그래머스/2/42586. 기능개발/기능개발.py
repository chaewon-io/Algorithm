import math

def solution(progresses, speeds):
    answer = []
    days_list = []

    for i in range(len(progresses)):
        days_list.append(math.ceil((100 - progresses[i]) / speeds[i]))

    while days_list:
        count = 1  # 배포 가능한 작업 수
        days = days_list.pop(0)  # 큐의 첫 번째 요소를 꺼내서 이 값을 기준으로 배포 날짜를 정함

        while days_list:
            if days >= days_list[0]:  # 첫 배포 날짜보다 작거나 같으면 배포 가능
                count += 1
                days_list.pop(0)
            else:
                break  
        answer.append(count) 

    return answer
