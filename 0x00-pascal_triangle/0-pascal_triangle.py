#!/usr/bin/python3
"""
pascale triangle project
"""
def pascal_triangle(n):
    """
    print the pascal triange
    """
    if isinstance(n, int):
        if (n > 0):
            pascal_list = [[1]]
            for i in range(1, n):
                new_list = []
                for j in range(i + 1):
                    if j == 0 or j == i:
                        new_list.append(1)
                    else:
                        new_list.append(pascal_list[i-1][j-1] + \
                                        pascal_list[i-1][j])
                    pascal_list.append(new_list)
            return pascal_list
        else:
            return []
    else:
        print("Please enter an integer")

