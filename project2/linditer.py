# Responsible student: Thor Lindberg (s170930)

def LindIter(System, N):
    
    '''
    Calculates N iterations of the system,
    according to the replacement rules for the Koch curve
    and Sierpinski triangle respectively.

    Parameters:
    System (string): Name of the Lindenmayer system, either Koch or Sierpinski.
    N (int): Number of iterations to be calculated.

    Returns:
    string: Output of the iteration.
    '''

    if System not in ['1', '2']:
        return print('\n' + 'You have entered an invalid option! Try again.')
    if System == '1':
        System = 'Koch'
    if System == '2':
        System = 'Sierpinski'

    try:
        N = int(N)
    except:
        return print('\n' + 'Number of iterations must be a number!')

    if int(N) > 6:
        return print('\n' + 'Maximum number of iterations exceeded!')
    if int(N) < 0:
        return print('\n' + 'Number of iterations must be positive!')

    curve = {
        'S': 'SLSRSLS',
        'L': 'L',
        'R': 'R'
    }

    triangle = {
        'A': 'BRARB',
        'B': 'ALBLA',
        'L': 'L',
        'R': 'R'
    }

    iteration = 0

    if System == 'Koch':
        LindenmayerString = 'S'
        while iteration < N:
            IterativeString = ''
            for letter in LindenmayerString:

                if letter not in curve:
                    IterativeString += letter

                if letter in curve:
                    IterativeString += curve[letter]

            LindenmayerString = IterativeString
            iteration += 1

    if System == 'Sierpinski':
        LindenmayerString = 'A'
        while iteration < N:
            IterativeString = ''
            for letter in LindenmayerString:

                if letter not in triangle:
                    IterativeString += letter

                if letter in triangle:
                    IterativeString += triangle[letter]

            LindenmayerString = IterativeString
            iteration += 1

    return LindenmayerString
