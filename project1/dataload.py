# Responsible student: William Bekmann (s184171)

def dataLoad(filename):

    import numpy as np
    from urllib.request import urlopen

    data = np.array([])
    lines = 0

    if filename.lower() == 'example':
        filename = urlopen(
            'https://drive.google.com/uc?export=download&id=1spjNRpXTHcr_4j9G8wjeLhX3G62y-KDd')
    else:
        filename = open(filename)

    for line in filename.readlines():
        line = line.rstrip()
        line = line.split()
        line = [float(index) for index in line]

        if 10 <= line[0] <= 60 and line[1] > 0 and line[2] in [1, 2, 3, 4]:
            data = np.append(data, [line[0], line[1], line[2]])

        lines += 1

        error = 'Error in line # ' + \
            str(lines) + '\n' + 'Data: ' + str(line) + '\n'

        if line[0] < 10:
            error += 'Error: ' + 'Temperature ' + \
                str(line[0]) + ' below 10' + '\n'
        if line[0] > 60:
            error += 'Error: ' + 'Temperature ' + \
                str(line[0]) + ' above 60' + '\n'
        if line[1] < 0:
            error += 'Error: ' + 'Negative growth rate ' + str(line[1]) + '\n'
        if line[2] not in [1, 2, 3, 4]:
            error += 'Error: ' + 'Bacteria ' + \
                str(line[2]) + ' not in the given table' + '\n'

        if error != 'Error in line # ' + str(lines) + '\n' + 'Data: ' + str(line) + '\n':
            print(error)

    data = data.reshape(int(np.size(data) / 3), 3)

    return data
