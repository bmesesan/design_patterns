# Given the following definition of a Node , please implement preorder traversal right inside Node.
# The sequence returned should be the sequence of values, not their containing nodes.

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        # todo - return inorder values (not Nodes)
        def traverse(current):
            yield (current)
            if current.left:
                for left in traverse(current.left):
                    yield (left)
            if current.right:
                for right in traverse(current.right):
                    yield (right)
        for node in traverse(self):
            yield (node.value)


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3
    # in-order: 213
    # preorder: 123
    # postorder: 231

    root = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, Node(6), Node(7)))

    for y in root.traverse_preorder():
        print(y)
