class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    nodeDistanceK = []
    findDistanceFromNodeToTarget(tree, target, k, nodeDistanceK)
    return nodeDistanceK


def findDistanceFromNodeToTarget(node, target, k, nodeDistanceK):
    if node is None:
        return -1

    if node.value == target:
        adddSubtreeNodeAtDistanceK(node, 0, k, nodeDistanceK)
        return 1

    leftDistance = findDistanceFromNodeToTarget(
        node.left, target, k, nodeDistanceK)
    rightDistance = findDistanceFromNodeToTarget(
        node.right, target, k, nodeDistanceK)

    if leftDistance == k or rightDistance == k:
        nodeDistanceK.append(node.value)

    if leftDistance != -1:
        adddSubtreeNodeAtDistanceK(
            node.right, leftDistance + 1, k, nodeDistanceK)
        return leftDistance + 1

    if rightDistance != -1:
        adddSubtreeNodeAtDistanceK(
            node.left, rightDistance + 1, k, nodeDistanceK)
        return rightDistance + 1

    return -1


def adddSubtreeNodeAtDistanceK(node, distance, k, nodeDistanceK):
    if node is None:
        return

    if distance == k:
        nodeDistanceK.append(node.value)
    else:
        adddSubtreeNodeAtDistanceK(node.left, distance + 1, k, nodeDistanceK)
        adddSubtreeNodeAtDistanceK(node.right, distance + 1, k, nodeDistanceK)
