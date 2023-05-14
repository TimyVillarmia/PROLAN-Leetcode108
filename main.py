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
    def sortedArrayToBST(nums: list[int]) -> BSTNode:
        def recursion(lower, upper):
            # base-case / stopping condition
            if lower > upper:
                return None

            # middle index of the array
            midpoint = (lower + upper + 1) // 2
            # create new BSTNode
            root = BSTNode(nums[midpoint])
            # recursive call for left subtree   
            root.left = recursion(lower, midpoint - 1)
            # recursive call for right subtree
            root.right = recursion(midpoint + 1, upper)
            return root

        return recursion(0, len(nums) - 1)


def inOrder(node):
    if not node:
        return
    # visit the left child/subtree recursively
    inOrder(node.left)
    # print the current node value
    print(node.val, end=" ")
    # then visit the right child/subtree recursively
    inOrder(node.right)


def main():
    # Testcases
    case1 = [-10, -3, 0, 5, 9]
    case2 = [1, 3]
    case3 = [-41, -32, -29, -20, -11, 0, 50, 65, 72, 91, 99]

    result = Solution
    print(inOrder(result.sortedArrayToBST(case1)))
    print(inOrder(result.sortedArrayToBST(case2)))
    print(inOrder(result.sortedArrayToBST(case3)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
