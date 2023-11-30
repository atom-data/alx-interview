#!/usr/bin/python3
"""
Define function island_perimeter
"""


def island_perimeter(grid):
    perimeter = 0
    for k in range(len(grid)):
        grid[k].insert(0, 0)
        grid[k].append(0)
    new_row = [0 for k in range(len(grid[0]))]
    grid.insert(0, new_row)
    grid.append(new_row)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
