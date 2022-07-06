'''
Made by: André Rosengaard Jørgensen
transform rotates a vector using the matrix in (2D.1)
Arguments: 
    someAngle: a number specifying the angle (in radians) the vector
    is to be rotated.
    someVector: a vector which is rotated
Output:
    transformVector: The rotated vector.
 '''

import numpy as np
import matplotlib.pyplot as plt

def turtlePlot(turtleCommands):

    currentpos = np.array([0, 0])
    vector = np.array([1, 0])
    fig, ax = plt.subplots()

    def transform(someAngle, someVector):

        transformArray = np.array([[np.cos(someAngle), np.sin(
            someAngle)], [-np.sin(someAngle), np.cos(someAngle)]])
        transformVector = np.dot(someVector, transformArray)
        return transformVector

    for i in range(len(turtleCommands)):
        
        if i == 0:
            newpos = currentpos + vector * turtleCommands[i]
            ax.plot([[currentpos[0]], [newpos[0]]], [
                    currentpos[1], newpos[1]], color='red')
            currentpos = newpos
            
        if i % 2 == 1:
            vector = transform(turtleCommands[i], vector)
            newpos = currentpos + vector * turtleCommands[i+1]
            ax.plot([[currentpos[0]], [newpos[0]]], [
                    currentpos[1], newpos[1]], color='red')
            currentpos = newpos
            i += 1

    ax.legend(['Turtle coordinates'])
    plt.title("Turtle plot")
    plt.show(block=False)
