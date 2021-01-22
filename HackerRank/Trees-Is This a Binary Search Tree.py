import math


def checkBST(root):
    def check(node, min, max):
        if not node:
            return True
        if node.data <= min or node.data >= max:
            return False
        return check(node.left, min, node.data) and check(node.right, node.data, max)
    return check(root, -math.inf, math.inf)
