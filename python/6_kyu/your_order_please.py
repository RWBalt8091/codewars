def order(sentence):
    if len(sentence) <= 0:
        return sentence
    else:
        test_list = sentence.split(' ')
        dict = {}
        for item in test_list:
            for char in item:
                try:
                    if int(char) > 0 and int(char) < 10:
                        dict[char] = item
                except:
                    pass
        output = ''
        sorted_dict = sorted(dict.items())
        last_key = sorted_dict[-1][0]
        for k, v in sorted_dict:
          if k != last_key:
              output = output + v + ' '
          else:
              output = output + v
        return output