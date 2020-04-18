# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        def isMirror(left, right):
            if left == None and right == None:
                return True
            elif left == None or right == None:
                return  False

            if left.val != right.val:
                return False
            #递归实现
            ret1 = isMirror(left.left, right.right)
            ret2 = isMirror(left.right, right.left)
            return ret1 and ret2
        if pRoot == None:
            return True

        return isMirror(pRoot.left, pRoot.right)