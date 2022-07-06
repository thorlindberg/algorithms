def tokenize(text):

    for index in range(len(text)):
        if text[index] == "'" and text[index-1] != 'c' and text[index+1] != 'h':
            text = text.replace(text[index-1] + text[index] + text[index+1], text[index-1] + ' ' + text[index+1])
    words = len(text.split(' '))

    return words