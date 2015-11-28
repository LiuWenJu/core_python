#coding=utf-8

def rebuild(pre, center):
    if not pre:
        return

    cur = Node(pre[0])
    index = center.index(pre[0], center[:index])
    cur.right = rebuild(pre[index + 1], center[index + 1:])
    return cur


def deep(root):
    if not root:
        return
    deep(root.left)
    deep(root.right)
    print root.data
