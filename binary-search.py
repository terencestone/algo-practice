

class Node:
    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        # if no root, make value the root
        if self.root == None:
            self.root = Node(value)
        # otherwise insert new value
        else:
            self._insert(value, self.root)

    def _insert(self, value, curr_node):
        # if the value is less than current root, insert left
        if value < curr_node.value:
            # and if there's no left child
            if not curr_node.left_child:
                # insert as left child
                curr_node.left_child = Node(value)
            # otherwise, keep moving down the tree until we can insert new value
            else:
                self._insert(value, curr_node.left_child)
        # otherwise it's a right node, go through same process
        elif value > curr_node.value:
            if not curr_node.right_child:
                curr_node.right_child = Node(value)
            else:
                self._insert(value, curr_node.right_child)
        else:
            print("Value already in tree.")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left_child)
            print(str(curr_node.value))
            self._print_tree(curr_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, curr_node, curr_height):
        if not curr_node: return curr_height
        left_height = self._height(curr_node.left_child, curr_height+1)
        right_height = self._height(curr_node.right_child, curr_height+1)
        return max(left_height, right_height)

    def search(self, value):
        # make sure tree exists
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, curr_node):
        # if value == current root, done
        if value == curr_node.value:
            return True
        # otherwise, if it's a left value (value < current root),
            # recursively search left side of tree
        elif value < curr_node.value and curr_node.left_child:
            return self._search(value, curr_node.left_child)
        # if it's a right value (value > current root),
            # recursively search right side of tree
        elif value > curr_node.value and curr_node.right_child:
            return self._search(value, curr_node.right_child)

        # if none of above, value is not in tree
        return False


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        curr_element = randint(0, max_int)
        tree.insert(curr_element)
    return tree

tree = BinarySearchTree()
# tree = fill_tree(tree)

values = [5,1,3,2,7,10,0,20]
for val in values:
    tree.insert(val)

tree.print_tree()

print(f'tree height: {tree.height()}')

print(tree.search(10))

print(tree.search(30))



