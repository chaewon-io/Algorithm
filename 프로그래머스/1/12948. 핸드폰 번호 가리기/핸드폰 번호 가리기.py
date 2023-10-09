def solution(phone_number):
    
    num = len(phone_number)
    hide_number = phone_number[-4:]
    
    return "*"*(num-4)+hide_number