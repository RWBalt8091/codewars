def song_decoder(song):
    x_list = song.split('WUB')
    y_list = []
    for items in x_list:
        if items != '':
            y_list.append(items)

    y_list_len = len(y_list)

    output = ''
    for index, items in enumerate(y_list):
        if index != y_list_len - 1:
            output = output + items + ' '
        else:
            output += items

    return output