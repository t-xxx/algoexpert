class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)


def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left

    return currentNode


def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None \
            and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent
