# Responsible student: Thor Lindberg (s170930)

def dataPlot(data):
  
    '''
    Outputs a bar plot and a line plot for the given data.

    Parameters:
    data (ndarray): A 2-dimensional array where each row equates to a record of
    temperature, growth rate, and a bacteria type.
    '''

    import numpy as np
    import matplotlib.pyplot as plt

    bacteria = {
        1: 'salmonella enterica',
        2: 'bacillus cereus',
        3: 'listeria',
        4: 'brochothrix thermosphacta'
    }

    count = []  # Assigns an empty list to the variable count.
    for key in bacteria:  # Loops through the keys in the bacteria dictionary.
        count.append(sum([row[2] for row in data if row[2] == key]))

    positions = np.arange(len(bacteria.keys()))
    figure1 = plt.figure(figsize=(7, 5))
    plt.bar(positions, count, 0.5)
    plt.grid(axis='y')
    plt.xticks(positions, bacteria.values())
    plt.ylabel('Number of bacteria')
    figure1.show()

    data = data[data[:, 0].argsort()]

    figure2 = plt.figure(figsize=(7, 5))
    for key in bacteria:
        temperatures = [row[0] for row in data if row[2] == key]
        rates = [row[1] for row in data if row[2] == key]
        plt.plot(temperatures, rates)

    plt.xlim((10, 60))
    plt.ylim(bottom=0)
    plt.grid(axis='y')
    plt.ylabel('Growth rate')
    plt.xlabel('Temperature')
    figure2.show()
