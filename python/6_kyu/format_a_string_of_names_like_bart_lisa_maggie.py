def namelist(names):
    if len(names) == 0:
        return ''
        
    elif len(names) == 1:
        formatted_names = []
        for index, strings in enumerate(names):
            x = dict()
            x.update(strings)
            formatted_names.append(x['name'])
        output = formatted_names[0]
        return output
        
    elif len(names) == 2:
        formatted_names = []
        for index, strings in enumerate(names):
            x = dict()
            x.update(strings)
            formatted_names.append(x['name'])
        
        output = formatted_names[0] + ' & ' + formatted_names[1]
        return output
        
    else:
        formatted_names = []
        for index, strings in enumerate(names):
            x = dict()
            x.update(strings)
            formatted_names.append(x['name'])
        
        names_length = len(formatted_names)
        
        output = ''
        for index, names in enumerate(formatted_names):
            if index == (names_length - 2):
                output = output + names + ' & '
            elif index == (names_length - 1):
                output = output + names
            else:
                output = output + names + ', '
        
        return output