# -*- coding:utf-8 -*-
# class Solution:
#    def NumberOf1(self, n):
# 补码：正数不变；负数是它的正数的反码+1
# "-2"的补码：
# 2 的二进制形式：1 00xx0010
# 2的反码：       1 11xx1101
# -2的补码：       1 11xx1110
# 分析：
# 正数的情况： 11110010

# n = 0xFFFFFFFF & n
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        #  抹掉最右边的一个1
        count = 0
        if n < 0:
            n = n & 0xFFFFFFFF
        while n:
            n = (n - 1) & n
            count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    ans = s.NumberOf1(-3)
    print(bin(ans))



