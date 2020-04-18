# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        #非法情况
        if pRoot2 == None or pRoot1 == None:
            return False

        def hasEqual(pRoot1, pRoot2):
            if pRoot2 == None:
                return True
            if pRoot1 == None:
                return False
            #要判断两个Root是否相等，先判断根节点是否相等
            if pRoot1.val == pRoot2.val:
                if pRoot2.left == None:
                    leftEqual = True
                else:
                    leftEqual = hasEqual(pRoot1.left, pRoot2.left) #左边相等
                if pRoot2.right == None:
                    rightEqual = True
                else:
                    rightEqual = hasEqual(pRoot1.right, pRoot2.right) #右边相等
                return leftEqual and rightEqual
            return False #不相等则返回false
        #判断根节点是否相等
        if pRoot1.val == pRoot2.val:
            ret = hasEqual(pRoot1, pRoot2)
            if ret:
                return True
        #判断左子树是否相等
        ret = self.HasSubtree(pRoot1.left, pRoot2)
        if ret:
            return True
        #判断右子树是否相等
        ret = self.HasSubtree(pRoot1.right, pRoot2)
        return ret

