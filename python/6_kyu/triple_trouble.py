def triple_double(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    
    len_num1 = len(num1)
    len_num2 = len(num2)
    
    num1_triple = 0
    for index in range(2, len_num1):
        if num1[index] == num1[index - 1] and num1[index] == num1[index - 2]:
            num1_triple = num1[index]
    
    if num1_triple == 0:
        return 0
    else:
        num2_triple = 0
        for index in range(2, len_num2):
            if num2[index] == num2[index - 1]:
                num2_triple = num2[index]
        
        if num1_triple == num2_triple:
            return 1
        else:
            return 0