import string
import numpy

def is_pangram(s):
    split_s = s.split(' ')
    letters = []
    for word in split_s:
        for char in word:
            if char.lower() == 'a' or char.lower() == 'b' or char.lower() == 'c' or char.lower() == 'd' or char.lower() == 'e' or char.lower() == 'f' or char.lower() == 'g' or char.lower() == 'h' or char.lower() == 'i' or char.lower() == 'j' or char.lower() == 'k' or char.lower() == 'l' or char.lower() == 'm' or char.lower() == 'n' or char.lower() == 'o' or char.lower() == 'p' or char.lower() == 'q' or char.lower() == 'r' or char.lower() == 's' or char.lower() == 't' or char.lower() == 'u' or char.lower() == 'v' or char.lower() == 'w' or char.lower() == 'x' or char.lower() == 'y' or char.lower() == 'z':                letters.append(char.lower())
            else:
                pass
    letters = sorted(letters)
    letters = numpy.unique(letters)
    
    if letters[0] == 'a' and letters[1] == 'b' and letters[2] == 'c' and letters[3] == 'd' and letters[4] == 'e' and letters[5] == 'f' and letters[6] == 'g' and letters[7] == 'h' and letters[8] == 'i' and letters[9] == 'j' and letters[10] == 'k' and letters[11] == 'l' and letters[12] == 'm' and letters[13] == 'n' and letters[14] == 'o' and letters[15] == 'p' and letters[16] == 'q' and letters[17] == 'r' and letters[18] == 's' and letters[19] == 't' and letters[20] == 'u' and letters[21] == 'v' and letters[22] == 'w' and letters[23] == 'x' and letters[24] == 'y' and letters[25] == 'z' :
        return True
    else:
        return False