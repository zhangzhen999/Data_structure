# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        #循环的出口
        preceise = 1
        highValue = 1
        midValue = 1
        lowValue = 1
        count = 0
        sumNum = 0
        while highValue != 0:
            highValue = n // (preceise * 10)
            midValue = (n // preceise) % 10
            lowValue = n % preceise
            preceise = preceise * 10

            if midValue == 0:
                #借一位
                num = (highValue -1 +1) * pow(10, count)
            elif midValue > 1:
                num = (highValue +1) * pow(10, count)
            else:
                num = (highValue) * pow(10, count) + lowValue + 1
            sumNum += num
            count += 1
        return sumNum

if __name__ == '__main__':
    s = Solution()
    numbers = 30
    ans = s.NumberOf1Between1AndN_Solution(numbers)
    print(ans)
