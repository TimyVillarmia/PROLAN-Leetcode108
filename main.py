# Definition for a binary tree node.
class BSTNode(object):
    # The __init__() function is called automatically every time the class is being used to create a new object.
    # Use the __init__() function to assign values to object properties,
    # or other operations that are necessary to do when the object is being created:
    # The self parameter is a reference to the current instance of the class,
    # and is used to access variables that belong to the class.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# reference https://www.youtube.com/watch?v=0K0uCMYq5ng
class Solution:
    def recursion(self, nums, lower, upper):
        # base-case / stopping condition
        if lower > upper:
            return None

        # middle index of the array
        midpoint = (lower + upper) // 2
        # create new BSTNode
        root = BSTNode(nums[midpoint])
        # recursive call for left subtree
        root.left = self.recursion(nums, lower, midpoint - 1)
        # recursive call for right subtree
        root.right = self.recursion(nums, midpoint + 1, upper)
        return root

    def sortedArrayToBST(self, nums: list[int]) -> BSTNode:
        return self.recursion(nums, 0, len(nums) - 1)


def inOrder(node):
    if not node:
        return
    # visit the left child/subtree recursively
    inOrder(node.left)
    # print the current node value
    print(node.val, end=" ")
    # then visit the right child/subtree recursively
    inOrder(node.right)


def preOrder(node):
    if not node:
        return
    # print the current node value
    print(node.val, end=" ")
    # visit the left child/subtree recursively
    postOrder(node.left)
    # then visit the right child/subtree recursively
    inOrder(node.right)


def postOrder(node):
    if not node:
        return

    # visit the left child/subtree recursively
    postOrder(node.left)
    # then visit the right child/subtree recursively
    inOrder(node.right)
    # print the current node value
    print(node.val, end=" ")


def main():
    # Testcases
    case1 = [-10, -3, 0, 5, 9]  # BST [0,-10,5,null,-3,null,9]
    case2 = [1, 3]  # BST [1,null,3]
    case3 = [3, 6, 8, 23, 48, 76, 89]  # BST [23,6,76,3,8,48,89]
    case4 = [-41, -32, -29, -20, -11, 0, 50, 65, 72, 91,99]  # BST [0,-29,72,-41,-20,50,91,null,-32,null,-11,null,65,null,99]
    case5 = [-20, -10, -3, 0, 5, 9, 27]  # BST [0,-10,9,-20,-3,5,27]

    result = Solution()
    print("Post-Order Traversal")
    print("Case #1: ")
    print(postOrder(result.sortedArrayToBST(case1)))
    print("Case #2: ")
    print(postOrder(result.sortedArrayToBST(case2)))
    print("Case #3: ")
    print(postOrder(result.sortedArrayToBST(case3)))
    print("Case #4: ")
    print(postOrder(result.sortedArrayToBST(case4)))
    print("Case #5: ")
    print(postOrder(result.sortedArrayToBST(case5)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
