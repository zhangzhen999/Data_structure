# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        #如果两个数相同，那么这两个数的异或运算就等于0
        # a ^ b ^ c == a ^ c ^ b
        if len(array) < 2:
            return None
        twoNumXor = None
        for num in array:
            if twoNumXor == None:
                twoNumXor = num
            else:
                twoNumXor = twoNumXor ^ num

        count =  0
        while twoNumXor % 2 == 0:
            twoNumXor = twoNumXor >> 1
            count += 1
        mask = 1 << count

        firstNum = None
        secondNum = None

        for num in array:
            if mask & num == 0:
                if

