import random
import timeit

class Node:
    right = None
    left = None
    value = 0

    def __init__(self, value):
        self.value = value


class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insertion(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.addNode(self.root, value)


    def addNode(self, root, value):
        if value > root.value:
            if root.right is not None:
                self.addNode(root.right, value)
            else:
                root.right = Node(value)
        elif value < root.value:
            if root.left is not None:
                self.addNode(root.left, value)
            else:
                root.left = Node(value)


    def search(self, value):
        if self.root is None:
            return False
        else:
            return self.checkNodeTest(self.root, value)


    # def checkNode(self, root, value):
    #     if root.value > value:
    #         if root.left is None:
    #             return False
    #         else:
    #             return self.checkNode(root.left, value)
    #     elif root.value < value:
    #         if root.right is None:
    #             return False
    #         else:
    #             return self.checkNode(root.right, value)
    #     else:
    #         return True

    def checkNodeTest(self, root, value):
        while root != None:
            if value > root.value:
                root = root.right

            elif value < root.value:
                root = root.left
            else:
                return True
        return False



    def inorder(self, root):
        if root:
            self.inorder(root.left)
            # print('root.value', root.value)
            self.inorder(root.right)


def generateRandomArray():
    arr = []
    for i in range(10000):
        ran = random.randint(1, 10000)
        arr.append(ran)
    return arr


tree = BinarySearchTree()

array = generateRandomArray()

def timeTreeSearch():
    print("100 is in the list. Is that correct?", tree.search(100))

def timeBinaryTreeSearch():
    for a in array:
        tree.insertion(a)

    tree.inorder(tree.root)

print('Tree Search', timeit.Timer(timeTreeSearch).timeit(number=100))
print('Binary Search Tree', timeit.Timer(timeBinaryTreeSearch).timeit(number=100))
