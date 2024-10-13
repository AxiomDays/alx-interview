#!/usr/bin/python3
def canUnlockAll(boxes):
    open = set([0])
    closed = set(boxes[0])

    while len(closed) > 0:
        key = closed.pop()

        if key not in open:
            open.add(key)
            closed = closed.union(boxes[key]).difference(open)

    return len(open) == len(boxes)
