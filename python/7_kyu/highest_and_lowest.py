import numpy as np
def high_and_low(numbers):
    split_numbers = numbers.split(' ')
    int_split_numbers = []
    
    for values in split_numbers:
        int_split_numbers.append(int(values))
        print(int_split_numbers)
    
    sorted_int_split_numbers = sorted(int_split_numbers)
    lowest = sorted_int_split_numbers[0]
    highest = sorted_int_split_numbers[-1]
    numbers = str(highest) + ' ' + str(lowest)
    return numbers