#!/usr/bin/python3
""" function that performs the aforementioned """
def canUnlockAll(boxes):
    """ function that checks if all boxes can be unlocked """
    open = set([0])
    closed = set(boxes[0]).difference(open)

    while len(closed) > 0:
        key = closed.pop()

        if key not in open:
            open.add(key)
            closed = closed.union(boxes[key]).difference(open)

    return len(open) == len(boxes)
