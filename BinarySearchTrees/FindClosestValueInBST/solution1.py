def findClosestValueInBst(tree, target):
    return explodeClosestValue(tree, target, tree.value)


def explodeClosestValue(tree, target, closestValue):
    print(closestValue)
    tree = compare_target_and_node(tree, target)

    if tree is None:
        print("1", closestValue)
        return closestValue
    else:
        existing_abs = abs(target - closestValue)
        new_abs = abs(target - tree.value)
        if existing_abs >= new_abs:
            closestValue = tree.value
        explodeClosestValue(tree, target, closestValue)


def compare_target_and_node(tree, target):
    if target > tree.value:
        return tree.right
    elif target < tree.value:
        return tree.left
    elif target == tree.value:
        return None

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
