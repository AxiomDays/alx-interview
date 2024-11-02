#!/usr/bin/python3
"""
module for checking the UTF-8 validity of a series of integers
"""

def validUTF8(data):
    """
    main function
    """
    temp = []
    for i in data:
        temp.append(dec2bin(i))
    """print(temp, end = ' ')"""
    if data == []:
        return True
    else:
        return checkUTF8(temp)

def dec2bin(num):
    """
    converts decimals to binary
    """
    temp = format(num,'08b')
    if len(format(num,'08b')) > 8:
        temp = format(num,'08b')[1:]
    return temp

def checkUTF8(templist):
    """
    checks each integer and if need be the subsequent integer
    """
    multibyte = 0
    truth = 0
    for elem in templist:
        truth = 0
        if multibyte > 0:
            if elem[:2] == '10' and multibyte == 1:
                truth = 1
                multibyte -= 1
                continue
            elif elem[:2] == '10':
                multibyte -= 1
                continue
            else:
                truth = 0
                break

        if elem[0] == '0':
            truth = 1
            continue

        if elem[:2] == '11':
            multibyte = 1
        else:
            truth = 0
            break

        if elem[2:4] == '10':
            multibyte = 2
        elif elem[2:5] == '110':
            multibyte = 3

    if (truth == 0):
        return (False)
    elif (truth == 1):
        return (True)

