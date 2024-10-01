#!/usr/bin/python3

"""
a function for pascal's triangle
"""

def runTheMiddle(sumlist):
    """ function that creates a list of the sum of the previous lists values, i.e the middle section of a pascal row """
    templist2 = []
    for k in range(len(sumlist)):
        if k == (len(sumlist)-1):
            break
        templist2.append(sumlist[k]+sumlist[k+1])

    return templist2


def pascal_triangle(n):
    """ main func """
    if n <= 0:
        return []

    mainlist = []

    for i in range(n):
        templist = []
        tempcounter = 0
        for j in range(i+1):
            if j == 0:
                """ each row always starts with 1 """
                templist.append(1)
            elif j != (i) and j > 0:
                """ only runs once, since it provides a list of the whole middle section """
                if tempcounter == 0:
                    templist.extend(runTheMiddle(mainlist[i-1]))
                    tempcounter = 1
            elif j == (i) and j > 0:
                """ each row ends with 1 """
                templist.append(1)
            else:
                continue
        mainlist.append(templist)

    return mainlist

