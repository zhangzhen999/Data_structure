# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None #指向父节点的指针next
class Solution:
    def GetNext(self, pNode):
        # case1. 寻找右子树，如果存在就一直找到右子树的最左边就是下一个节点
        # case2. 如果没有右子树，就寻找他的父节点，一直找到它的父节点的左子树，打印父节点
        if pNode.right:
            #找右子树
            tmpNode = pNode.right
            while tmpNode.left:
                #找右子树的左节点
                tmpNode = tmpNode.left
            return tmpNode
        else:
            #没有右子树
            tmpNode = pNode
            #遍历他的父节点
            while tmpNode.next:
                #如果节点PNode（tmpNode)的父节点tmpNode.next的left等于，如上图中index= 2 的节点
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                #如果节点tmpNode的父节点的左节点 不等于他自身，那么就将父节点作为当前节点tmpNode，如上图中index=3的节点
                tmpNode = tmpNode.next
            return None

