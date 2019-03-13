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

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
        return f"({root.val},{serialize(root.left)},{serialize(root.right)})" if root else None

def deserialize(string):
    if string == "None": return None

    val = 0
    commas = []

    for idx, elt in enumerate(string):
        if elt == "(" : val+=1
        if elt == ")" : val-=1
        if val == 1 and elt == "," :
            commas.append(idx)

    return Node(string[1:commas[0]], deserialize(string[commas[0]+1:commas[1]]), deserialize(string[commas[1]+1:-1]))

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
