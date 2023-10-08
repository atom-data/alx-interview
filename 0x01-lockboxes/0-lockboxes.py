#!/usr/bin/python3
"""
Determine if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    n = len(boxes)
    myList = [0]
    for i in myList:
        for j in boxes[i]:
            if j not in myList:
                if j < n:
                    myList.append(j)
    if len(myList) == n:
        return True
    return False
