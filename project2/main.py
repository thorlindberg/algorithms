# Responsible student: Thor Lindberg (s170930)

from turtlePlot import turtlePlot
from turtleGraph import turtleGraph
from LindIter import LindIter
import os
directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory)


print('Welcome to our program for computing and plotting Lindenmayer systems!')
LindenmayerString = False

while True:

    print('\n' + 'Input the number of one of the options below.')
    print('[1] Choose a type of Lindenmayer system and the number of iterations.')
    print('[2] Generate plot.')
    print('[3] Quit.' + '\n')
    option = input('Input: ')

    if option not in ['1', '2', '3']:
        print('\n' + 'You have entered an invalid option! Try again.')
        continue

    if option == '1':
        while True:

            print('\n' + 'Input the number of one of the systems below.')
            print('[1] Koch')
            print('[2] Sierpinski' + '\n')
            System = input('Input: ')

            print('\n' + 'Input the number of iterations below.')
            print('Note: maximum number of iterations is 6!' + '\n')
            N = input('Input: ')

            print('\n' + 'Creating your Lindenmayer string ...')
            LindenmayerString = LindIter(System, N)
            if isinstance(LindenmayerString, str) == True:
                print('\n' + 'Lindenmayer string has been created!')
                break

    if option == '2':

        if LindenmayerString == False:
            print(
                '\n' + 'You must choose a type of system and a number of iterations before generating plots!')
            continue

        print('\n' + 'Creating your plot ...')
        turtleCommands = turtleGraph(LindenmayerString, int(N))
        turtlePlot(turtleCommands)
        print('\n' + 'Plot has been created!')

    if option == '3':

        print('\n' + 'Thank you for using our program!')
        print('Program has been terminated.')
        break
