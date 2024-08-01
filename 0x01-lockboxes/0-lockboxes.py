#!/usr/bin/python3
"""
Lockbox project
"""


def canUnlockAll(boxes):
    """
    solving Lockbox project
    """
    open_boxes = [boxes[0]]
    for box in open_boxes:
        for key in box:
            for j in range(len(boxes)):
                if boxes[j] not in open_boxes:
                    if key == j or len(boxes[j]) == 0:
                        open_boxes.append(boxes[j])
                    j = j+1
                else:
                    continue
    if (len(open_boxes) == len(boxes)):
        return True
    else:
        return False
