def packing(box, object):

    import numpy as np
    
    reverse = object[::-1]
    d1 = object - box
    d2 = reverse - box
    d1[d1 <= 0] = 0
    d2[d2 <= 0] = 0

    if np.sum(d1) < np.sum(d2):
        d = d1
    if np.sum(d1) > np.sum(d2):
        d = d2
    if np.sum(d1) == np.sum(d2):
        d = d1
    
    return d