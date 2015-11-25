#coding=utf-8

from node import Node
#求最大树深

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))



def maxDepth(root):

    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1



if __name__=="__main__":
    maxDepth(tree)
