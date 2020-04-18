# -*- coding:utf-8 -*-

class Solution:
    def Add(self, num1, num2):
        xorNum = num1 ^ num2
        andNum = (num1 & num2) << 1
        while andNum != 0:
            tmp1 = xorNum ^ andNum
            tmp2 = (xorNum & andNum) << 1 # &运算后进位
            tmp1 = tmp1 & 0xFFFFFFFF #负数的情况
            xorNum = tmp1
            andNum = tmp2

        # return xorNum if xorNum <= 0x7FFFFFFF else xorNum - 0x100000000
        return xorNum if xorNum <= 0x7FFFFFFF else ~(xorNum ^ 0xFFFFFFFF)
if __name__ == '__main__':
    s = Solution()
    ans = s.Add(-7,17)
    print(ans)

