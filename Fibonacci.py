class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
    #     if n > 1:
    #         num = self.Fibonacci(n - 1) + self.Fibonacci(n - 2)
    #         return num
    #     return none
        if n > 1:
            a=0
            b=1
            ret=0
            for i in range(0,n-1):
                ret=a+b
                a=b
                a=ret
            return ret

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(10))
