# -*- coding:utf-8 -*-
"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        #dict [key] = count
        numsCount = {}
        numLen = len(numbers)

        for num in numbers:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
            if numsCount[num] > (numLen >> 1):
                return num
        return 0

if __name__ == '__main__':
    s = Solution()
    numbers = [1,2,3,2,2,2,5,4,2]
    ans = s.MoreThanHalfNum_Solution(numbers)
    print(ans)

"""

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        last = 0
        lastCount = 0

        for num in numbers:
            if lastCount == 0:
                last = num
                lastCount = 1
            else:
                if num == last:
                    lastCount += 1
                else:
                    lastCount -= 1

        if lastCount == 0:
            return 0
        else:
            #这种情况是last可能是大于一半的数字
            lastCount = 0
            for num in numbers:
                if num == last:
                    lastCount += 1
            if lastCount > (len(numbers) >> 1):
                return last
        return 0

if __name__ == '__main__':
    s = Solution()
    numbers = [1,2,3,2,2,2,5,4,2]
    ans = s.MoreThanHalfNum_Solution(numbers)
    print(ans)