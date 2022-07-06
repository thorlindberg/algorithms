import sys
import os
directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(directory)

try:
    import numpy as np
    from urllib.request import urlopen
    import matplotlib.pyplot as plt
    from dataLoad import dataLoad
    from dataStatistics import dataStatistics
    from dataPlot import dataPlot
except:
    sys.exit('Error! Program requires modules: numpy, urllib, matplotlib, dataLoad, dataStatistics, dataPlot')

print('Welcome to our data analysis program!' + '\n')
filterActive = False
loaded = False

while True:

    print('Please input one of the following options:' + '\n')
    print('Load data')
    print('Filter data')
    print('Display statistics')
    print('Generate plots')
    print('Documentation')
    print('Quit' + '\n')

    if filterActive != False:
        print('Active filter: ' + filterActive)
        print('Input remove filter to disable your filter.' + '\n')

    option = input('Input: ').lower()

    if option not in ['load data', 'filter data', 'display statistics', 'generate plots', 'documentation', 'quit', 'remove filter']:
        print('\n' + 'Error! Your input "' +
              option + '" is not an option.' + '\n')

    if option == 'remove filter' and filterActive == False:
        print('\n' + 'Error! You do not have an active filter.' + '\n')
    if option == 'remove filter' and filterActive != False:
        print('\n' + 'Your filter has been succesfully removed.' + '\n')
        data = original
        filterActive = False

    if option == 'load data':
        while True:

            print('\n' + 'Please input the name of the file:')
            print('Alternatively, input example to use an example.' + '\n')

            filename = input('Input: ')

            print('\n' + 'Loading the file ...' + '\n')

            try:
                data = dataLoad(filename)
            except:
                print('Error! You have entered an invalid file.')
                continue

            original = data
            print('You have succesfully loaded the file!' + '\n')
            loaded = True
            break

    if option == 'filter data':
        while True:

            if loaded != True:
                print('\n' + 'Error! You can not filter before loading a file.' + '\n')
                break

            print('\n' + 'Note! Filtering twice will remove the previous filter.')
            print('Please input a filter from the following options:' + '\n')
            print('Bacteria type')
            print('Growth rate range' + '\n')
            condition = input('Input: ').lower()

            if condition not in ['bacteria type', 'growth rate range']:
                print('\n' + 'Error! Your input "' +
                      condition + '" is not an option' + '\n')
                continue

            if condition == 'bacteria type':

                bacteria = {
                    'salmonella enterica': 1,
                    'bacillus cereus': 2,
                    'listeria': 3,
                    'brochothrix thermosphacta': 4
                }

                print(
                    '\n' + 'Please input a type of bacteria from the following options:' + '\n')
                print('Salmonella enterica')
                print('Bacillus cereus')
                print('Listeria')
                print('Brochothrix thermosphacta' + '\n')
                bacteriaType = input('Input: ').lower()

                if bacteriaType in bacteria:

                    data = original
                    filterActive = False

                    data = np.array(
                        [row for row in data if row[2] == bacteria[bacteriaType]])
                    print('\n' + 'Your filter has been applied.' + '\n')
                    filterActive = 'bacteria type "' + str(bacteriaType) + '"'
                    break

                if bacteriaType not in bacteria:
                    print('\n' + 'Error! You have entered an invalid type of bacteria.')
                    continue

            if condition == 'growth rate range':

                print('\n' + 'Please input a lower bound for range:' + '\n')
                lower = input('Input: ')

                try:
                    lower = float(lower)
                except ValueError:
                    print('\n' + 'Error! Your input "' + lower +
                          '" is not a valid bound.' + '\n')
                    continue
                lower = float(lower)

                print('\n' + 'Please input an upper bound for range:' + '\n')
                upper = input('Input: ')

                try:
                    upper = float(upper)
                except ValueError:
                    print('\n' + 'Error! Your input "' + upper +
                          '" is not a valid bound.' + '\n')
                    continue

                upper = float(upper)

                if lower < upper:

                    data = original
                    filterActive = False

                    data = np.array(
                        [row for row in data if lower <= row[1] <= upper])
                    print('\n' + 'Your filter has been applied.' + '\n')
                    filterActive = 'growth rate range from ' + \
                        str(lower) + ' to ' + str(upper) + ' (inclusive)'
                    break

                if lower >= upper:
                    print('Error! You have entered an invalid upper and lower bound.')
                    continue

    if option == 'display statistics':
        while True:

            if loaded != True:
                print(
                    '\n' + 'Error! You can not display statistics before loading a file.' + '\n')
                break

            statistics = ['mean temperature', 'mean growth rate', 'std temperature',
                          'std growth rate', 'rows', 'mean cold growth rate', 'mean hot growth rate']

            print(
                '\n' + 'Please input a statistic method from the following options:' + '\n')
            for statistic in statistics:
                print(statistic.title())
            print('')

            statistic = input('Input: ').lower()

            if statistic not in statistics:
                print('\n' + 'Error! Your input "' +
                      statistic + '" is not an option' + '\n')
                continue

            if statistic in statistics:
                print('\n' + statistic.title() + ': ' +
                      str(dataStatistics(data, statistic)) + '\n')
                break

    if option == 'generate plots':
        while True:

            if loaded != True:
                print(
                    '\n' + 'Error! You can not generate plots before loading a file.' + '\n')
                break

            print('')
            dataPlot(data)
            print('')
            break

    if option == 'documentation':

        print('\n' + 'Below is the documentation for the options in the program.' + '\n')
        print('Operation \t\t Function')
        print('--------- \t\t --------')
        print('Load data \t\t Receives a file name, and loads the file into the program.')
        print(
            'Filter data \t\t Displays a list of filters, and applies the selected filter.')
        print('Display Statistics \t Displays a list of statistic methods, and applies the selected method.')
        print('Generate Plots \t\t Displays two plots for the data in the loaded file.')
        print('Documentation \t\t Displays this table, documenting the function of the operations in the program.')
        print('Quit \t\t\t Terminates the program.')
        print('')

    if option == 'quit':

        print('\n' + 'Thank you for making us your choice of data analysis program!')
        print('Program has been succesfully terminated.')
        break
