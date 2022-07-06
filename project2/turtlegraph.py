# Made by William (s84171)

def turtleGraph(LindenmayerString, N):

    import numpy as np
    import math

    turtleCommands = np.array([])

    if 'S' in LindenmayerString:
        Koch = {
            'S': 1 * ((1 / 3) ** N),
            'L': math.pi * (1 / 3),
            'R': math.pi * (-2 / 3)
        }

    Sierpinski = {
        'A': 1 * (1 / 2) ** N,
        'B': 1 * (1 / 2) ** N,
        'L': math.pi * (1 / 3),
        'R': math.pi * (-1 / 3)
    }

    if 'S' in LindenmayerString:
        for letter in LindenmayerString:
            turtleCommands = np.append(turtleCommands, Koch[letter])

    if 'A' in LindenmayerString:
        for letter in LindenmayerString:
            turtleCommands = np.append(turtleCommands, Sierpinski[letter])

    return turtleCommands
