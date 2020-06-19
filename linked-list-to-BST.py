'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5


'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
O(n log n) solution
'''
class Solution:

    def find_middle(self, head):
        # prev is set to none
        # slow and fast both set to head
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head

        # slow_ptr moves one node at a time
        # while fast_ptr moves 2 nodes at a time
        # by the time fast ptr reaches end of list, slow will be at middle
        # we preserve node (prev_ptr) right before slow_ptr so we can split list later
        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # this disconnects the portion of the list to the left of the middle
        # if prv_ptr exists after loop, it will point to one node before mid,
        # hence splitting the list
        if prev_ptr:
            prev_ptr.next = None

        # returns middle element
        return slow_ptr

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # this will occur on last element of each half

        # if head if no head, return null
        if not head:
            return None

        # find middle element for list
        mid = self.find_middle(head)

        # middle becomes root tree node
        node = TreeNode(mid.val)

        # if only one element, return the node
        if head == mid: return node

        # recursively sort left and right halves of original list:
        # pass original head (which is now split representing left half)
        node.left = self.sortedListToBST(head)
        # pass element after mid (which is now right half)
        node.right = self.sortedListToBST(mid.next)

        return node

'''
O(n) solution; Inorder Simulation;

"Elements processed in the inorder fashion on a binary search tree turn out to be sorted in ascending order."

Reason we can use this is ONLY BC we are given an ordered linked list

'''
class Solution_2:

    def find_size(self, head):
        # just count the elements
        ptr = head
        count = 0
        while ptr:
            ptr = ptr.next
            count += 1

        return count


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.find_size(head)

        # Recursively form a BST out of linked list from start --> end
        def convert(l, r):
            # make head nonlocal
            nonlocal head

            # Invalid case (if start is greater than end)
            if l > r: return None

            # find the middle element by halfing the list to floored val
            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node left
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm,
            # i.e. progress current value forward
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)

            # return the node
            return node

        # convert the original list
        return convert(0, size - 1)