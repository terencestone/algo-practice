class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return f'(data: {self.data}, next: {str(self.next)})'

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        if not self.head:
            return str([])

        l = []
        current = self.head
        while current:
            l.append(str(current))
            if current.next:
                current = current.next
            else:
                current = None

        return str(l)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        head = self.head
        if not head: return
        if head.data == data:
            self.head = head.next
            return

        current = head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next

            current = current.next

def merge_sort(h):
    if not h or not h.next: return h

    mid = get_middle(h)
    right_half = mid.next
    mid.next = None

    left = merge_sort(h)
    right = merge_sort(right_half)

    result = sorted_merge(left, right)

    return result

def sorted_merge(left, right):
    if not left: return right
    if not right: return left

    result = None
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)

    return result

def get_middle(h):
    if not h: return h

    fast = h
    slow = h

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# run
import random

length = random.randint(0,100)
l = LinkedList()
for _ in range(0,length):
    l.append(random.randint(0, 100))

print(merge_sort(l.head))
