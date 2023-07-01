#!/usr/bin/python3

def pascal_triangle(n):
    """
        pascal_triangle : function that returns a pascal triangle
   """
    pascal_list = []
    if n <= 0:
        return (pascal_list)
    for i in range(1, n + 1):
        coeff = 1
        row = []
        for j in range(1, i + 1):
            row.append(coeff)
            coeff = coeff * (i - j) // j
        pascal_list.append(row)
    return (pascal_list)
