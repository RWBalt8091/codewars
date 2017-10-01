def solution(number):
    number_list = []
    for digit in range(0,number):
        if digit % 3 == 0 or digit % 5 == 0:
            number_list.append(digit)
        else:
            pass
    
    return sum(number_list)