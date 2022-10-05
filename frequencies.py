"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    itemsStr = []
    for i in items:
        itemsStr.append(str(i))

    for i in itemsStr:
        count = itemsStr.count(i)
        print(count)
        frequencies[i] = count


    return frequencies
