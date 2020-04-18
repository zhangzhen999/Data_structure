"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return None
        #### 死循环，找丑数
        #### 判断一个数是不是丑数，先循环除以2，直到不能整除
        #### 循环除以3，直到不能整除，循环除以5，直到不能整除
        #### 这是如果剩余的值是1，我们就说它是丑数
        #### 其他情况都不是丑数
        count = 0
        def isUglyNumber(num):
            while num % 2 == 0:
                num = num // 2
            while num % 3 == 0:
                num = num // 3
            while num % 5 == 0:
                num = num // 5
            if num == 1:
                return True
            else:
                return False

        num = 1
        while True:
            if isUglyNumber(num):
                count += 1
            if count == index:
                return num
            num += 1

if __name__ == '__main__':
    s = Solution()
    ans = s.GetUglyNumber_Solution(17)
    print(ans)

"""

class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        uglyList = [1]
        count = 1
        twoPointer = 0
        threePointer = 0
        fivePointer = 0
        while count != index:
            minValue = min( 2 * uglyList[twoPointer], 3 * uglyList[threePointer], 5 * uglyList[fivePointer])
            uglyList.append(minValue)
            count += 1
            if minValue == 2 * uglyList[twoPointer]:
                twoPointer += 1

            if minValue == 3 * uglyList[threePointer]:
                threePointer += 1

            if minValue == 5 * uglyList[fivePointer]:
                fivePointer += 1
        return uglyList[count - 1]

if __name__ == '__main__':
    s = Solution()
    ans = s.GetUglyNumber_Solution(4)
    print(ans)