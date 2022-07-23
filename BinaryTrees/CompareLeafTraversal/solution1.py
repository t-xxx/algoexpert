class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)

    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False

        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right

    return list1CurrentNode is None and list2CurrentNode is None


def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode

    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode

        previousNode = currentNode

    leftHead, leftPreviousNode = connectLeafNodes(
        currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)


def isLeafNode(node):
    return node.left is None and node.right is None
