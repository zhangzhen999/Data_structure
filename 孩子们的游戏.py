# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        #通过推导公式可得f(n) = (f(n-1) + m)%n
        if n < 1 or m < 1:
            return -1
        if n == 1:
            return 0
        value = 0

        for index in range(2, n+1):
            currentValue = (value + m) % index
            value = currentValue
        return value

