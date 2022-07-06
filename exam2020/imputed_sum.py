def imputed_sum(x):

    import numpy as np

    s = []
    for index in range(len(x)):
        if x[index] == 999 and index == 0:
            s.append(x[index+1])
        if x[index] == 999 and index == len(x)-1:
            s.append(x[index-1])
        if x[index] == 999 and index not in [0, len(x)-1]:
            s.append(np.mean([x[index-1], x[index+1]]))
        if x[index] != 999:
            s.append(x[index])
    s = np.sum(s)

    return s