# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None:
            return []
        #辅助列表
        support = [root]
        ret = []

        while support:
            tmpNode = support[0]
            ret.append(tmpNode.val)

            if tmpNode.left:
                support.append(tmpNode.left)
            if tmpNode.right:
                support.append(tmpNode.right)
            del support[0]

        return ret