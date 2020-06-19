'''
Write a function that determines whether the left or right branch of the tree is larger.
The size of each branch is the sum of the node vlaues.
The function should return the string “Right” if the right side is larger and “Left” if the left side is larger.
If the tree has zero nodes or if the size of the branches are equal, an empty string “” should be returned.

For example, [3, 6, 2, 9, -1, 10] represents the following binary tree, where -1 indicates it is a NULL node.

     3
  6    2
9    10
'''
def solution(arr):
    if not arr:
        return ""

    def sum(arr, idx):
        # if we're not at end of list, initiate check
        if idx - 1 < len(arr):
            # if empty node (signified by -1), return 0
            if arr[idx - 1] == -1:
                return 0

            # we know that the left tree index will always be the parent's index * 2
            # we know that the right tree idx will always be the parent's idx * 2 + 1
            # for the current idx, return the prior element (parent)
                #  + recursive sum of the left tree
                #  + recursive sum of right tree
                # FOR THE GIVEN PARENT (which could be on the highest level left or right side)
            return arr[idx - 1] + sum(arr, idx * 2) + sum(arr, idx * 2 + 1)
        return 0

    # we can isolate each side by starting with the appropriate index
    # for a binary tree, the left always starts with index 2, and right index 3
    left = sum(arr, 2)
    right = sum(arr, 3)


    # conditionally return empty string, "left", or "right"
    if left == right:
        return ""
    else:
        if left > right:
            return "Left"
        else:
            return "Right"
