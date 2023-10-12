#!/usr/bin/python3

"""
This file contains a script to calculate the minimum or
fewest number of operations neded to result in exactly n 'H'
characters in the file
"""


def minOperations(n):
    """
        Function_Name - minOperations
        Arguments:
            n ( Integer )
        Returns:
            Integer
    """
    num_of_operations = 0
    clipboard = 0
    while(n > 1):
        if (clipboard > 0 and n/clipboard):
            n = n//clipboard
            num_of_operations += clipboard
        else:
            f = largestFactor(n)
            n = n//f
            num_of_operations += f
            clipboard = f
    return num_of_operations


def largestFactor(n):
    """
        Function_Name - largestFactor
        Arguments:
            n ( Integer)
        Returns:
            Integer
    """
    factor = 1
    for i in range(1, n):
        if (n % i == 0):
            factor = i
    return factor
