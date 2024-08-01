#!/usr/bin/python3
"""
Lockbox project
"""


def canUnlockAll(boxes):
    """
    solving Lockbox project
    """
    n = len(boxes)
    open_boxes = [boxes[0]]
    for box in open_boxes:
        for key in box:
            for j in range(n):
                if boxes[j] not in open_boxes:
                    if key == j or len(boxes[j]) == 0:
                        open_boxes.append(boxes[j])
                else:
                    continue
    if len(open_boxes) == n:
        return True
    return False
