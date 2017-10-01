def getCount(inputStr):
    num_vowels = 0
    inputStr = str(inputStr)
    
    for x in inputStr.lower():
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x =='u':
            num_vowels += 1

    return num_vowels