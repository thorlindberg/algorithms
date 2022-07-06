def dice_sum_count(threshold, dice):

    import numpy as np
    
    combinations = []
    if dice == 1:
        for die1 in range(1, 7):
            combinations.append([die1])

    if dice == 2:      
        for die1 in range(1, 7):
            for die2 in range(1, 7):
                combinations.append([die1, die2])
    
    if dice == 3:
        for die1 in range(1, 7):
            for die2 in range(1, 7):
                for die3 in range(1, 7):
                    combinations.append([die1, die2, die3])

    combinations = [np.sum(combination) for combination in combinations]
    count = len([combination for combination in combinations if combination <= threshold])

    return count