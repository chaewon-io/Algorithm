def solution(my_string):
    colletion = ("a,e,i,o,u")
    for i in colletion:
        my_string = my_string.replace(i, "")
    return my_string