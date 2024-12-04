#!/usr/bin/python3
"""
island perimeter main function
"""

def island_perimeter(grid):
    """
    funtion that checks the perimeter
    of an island made of 1s
    """
    perimeter = 0

    width = len(grid[0])
    length = len(grid)

    for i in range(length):
        for j in range(width):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == (width-1) or grid[i][j+1] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if i == (length-1) or grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter
