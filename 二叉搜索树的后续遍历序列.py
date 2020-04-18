"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return True
        rootNum = sequence[-1]
        del sequence[-1]
        # 找一个索引将左子树和右子树分开
        index = None
        for i in range(len(sequence)):
            if index == None and sequence[i] > rootNum:
                index = i
                # break
                #继续循环，看后面的值是否都大于rootNum
            if index != None and sequence[i] < rootNum:
                return False

        leftRet = self.VerifySquenceOfBST(sequence[:index])

        rightRet = self.VerifySquenceOfBST(sequence[index:])

        return leftRet and rightRet
"""

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        rootNum = sequence[-1]
        del sequence[-1]
        # 找一个索引将左子树和右子树分开
        index = None
        for i in range(len(sequence)):
            if index == None and sequence[i] > rootNum:
                index = i
                # break
                #继续循环，看后面的值是否都大于rootNum
            if index != None and sequence[i] < rootNum:
                return False
        if sequence[:index] == []:
            leftRet = True
        else:
            leftRet = self.VerifySquenceOfBST(sequence[:index])
        if sequence[:index] == []:
            rightRet = True
        else:
            rightRet = self.VerifySquenceOfBST(sequence[index:])

        return leftRet and rightRet