def riemann(n, form):

    import numpy as np
    import math

    s = []
    if form == 'a':
        for i in range(1, n + 1):
            s.append(((-1)**(i+1)) / math.ceil(i/2))
    if form == 'b':
        for i in range(1, n + 1):
            s.append((-1)**(i+1) / (i))
    s = np.sum(s)

    return s