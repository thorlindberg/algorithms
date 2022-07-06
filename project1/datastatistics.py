# Responsible student: André Jørgensen (s183451)

def dataStatistics(data, statistic):
  
    '''
    Returns either computed mean or standard deviation from a given criteria or the number of rows in the data array.
    Temperature corresponds to first column, growth rate to the second.
    Cold growth rate only accepts temperatures lower than 20. Hot only accepts temperatures higher than 50.

    Parameters:
    data : an nx3 array, with each column assigning a value to temperature, growth rate or type, respectively.
    statistic : a string defining which computation to make.

    Output:
    result : the result of the computation in the form af a float.
    '''

    import numpy as np

    statistics = {
        'mean temperature': np.mean(data[:, 0]),
        'mean growth rate': np.mean(data[:, 1]),
        'std temperature': np.std(data[:, 0]),
        'std growth rate': np.std(data[:, 1]),
        'rows': np.size(data, 0),
        'mean cold growth rate': np.mean([row[1] for row in data if row[0] < 20]),
        'mean hot growth rate': np.mean([row[1] for row in data if row[0] > 50])
    }

    result = statistics[statistic.lower()]

    return result
