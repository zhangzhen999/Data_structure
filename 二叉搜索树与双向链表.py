# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return

        def find_right(node):
            while node.right:
                node = node.right
            return node

        #递归
        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)

        # 根节点
        retNode = leftNode
        #左子树节点不为空的情况，找到最右节点，右子树不变
        if leftNode:
            leftNode = find_right(leftNode)
        else:
            retNode = pRootOfTree

        pRootOfTree.left = leftNode #将左子树的最右节点赋值给跟节点的左节点

        pRootOfTree.right = rightNode #右子树不变

        #双向链表
        if leftNode != None:
            leftNode.right = pRootOfTree
        if rightNode != None:
            rightNode.left = pRootOfTree

        return retNode
