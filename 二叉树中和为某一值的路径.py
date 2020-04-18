# -*- coding:utf-8 -*-
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        if root == None:
            return []

        ret = []
        #保存路径的值
        supportArraryList = [[root.val]]
        #保存路径的节点Node，用来做广度优先遍历
        support = [root]
        while support:
            tmpNode = support[0]
            tmpArrayList = supportArraryList[0]

            if tmpNode.left == None and tmpNode.right == None:
                if sum(tmpArrayList) == expectNumber:
                    ret.insert(0, tmpArrayList)

            #广度优先遍历
            if tmpNode.left:
                #append节点Node
                support.append(tmpNode.left)
                #append列表  路径值
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.left.val)
                supportArraryList.append(newTmpArrayList)
            if tmpNode.right:
                support.append(tmpNode.right)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(tmpNode.right.val)
                supportArraryList.append(newTmpArrayList)

            del supportArraryList[0]
            del support[0]
        return ret