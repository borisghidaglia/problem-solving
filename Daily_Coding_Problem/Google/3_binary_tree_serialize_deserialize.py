""" This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import re

# NOTE: We could have created a BinaryTree class, but as it is not stated, we tried to stay
# as close as possible to the problem subject => however, we had to add a second
# parameter
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
        return f"({root.val},{serialize(root.left)},{serialize(root.right)})" if root else None

# def deserialize(string):
#     while re.findall(r'\(([\(A-z.]+,)([A-z.]+,)([A-z.]+)\)', string):
#         for match in re.findall(r'\(([\(A-z.]+,)([A-z.]+,)([A-z.]+)\)', string):
#             val, left, right = match[0].replace(',', ''), match[1].replace(',', ''), match[2]
#             node = Node(val, left=left, right=right)
#             re.sub(r'\(([\(A-z.]+,)([A-z.]+,)([A-z.]+)\)', node, string)

def deserialize(string):
    # if isinstance(string, str):
    #     string = string.split(',')
    # print(string)
    # print(string[0], deserialize(string[1:]), deserialize(string[2:]))
    # for i in reversed(range(-3, len(node_vals), -3)):
    #     print(node_vals[i], node_vals[i+1], node_vals[i+2])
    return ''

node = Node('root', Node('left', Node('left.left')), Node('right'))
string = serialize(node)
print(string)
print(deserialize(string))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
