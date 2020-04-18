# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        #大数放到小堆里，小数放到大堆里
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        #有两种case：1是最大堆的节点数>最小堆的，case2：最大堆数= 最小堆数
        if self.maxHeapCount > self.minHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tmpNum)
            else:
                self.createMinHeap(num)
        else:
            self.maxHeapCount += 1
            if len(self.littleValueMaxHeap) == 0:
                self.createMaxHeap(num)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tmpNum)
                else:
                    self.createMaxHeap(num)
        #print(self.littleValueMaxHeap)
        #print(self.bigValueMinHeap)

    def GetMedian(self, n = None):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return float(self.littleValueMaxHeap[0] + self.bigValueMinHeap[0]) / 2

    #堆插入的函数
    def createMaxHeap(self, num):
        self.littleValueMaxHeap.append(num)
        tmpIndex = len(self.littleValueMaxHeap) - 1  #找出最大堆中最后的一个数给定一个索引 index
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if self.littleValueMaxHeap[parentIndex] < self.littleValueMaxHeap[tmpIndex]:
                self.littleValueMaxHeap[parentIndex], self.littleValueMaxHeap[tmpIndex] = \
                    self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMaxHeap(self, num):
        if num < self.littleValueMaxHeap[0]:
            maxHeapLen = len(self.littleValueMaxHeap)
            self.littleValueMaxHeap[0] = num
            tmpIndex = 0
            while tmpIndex < maxHeapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                largerIndex = 0
                if rightIndex < maxHeapLen:
                    largerIndex = rightIndex if self.littleValueMaxHeap[leftIndex] < self.littleValueMaxHeap[rightIndex] else leftIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break

                if self.littleValueMaxHeap[tmpIndex] < self.littleValueMaxHeap[largerIndex]:
                    self.littleValueMaxHeap[largerIndex], self.littleValueMaxHeap[tmpIndex] = self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[largerIndex]
                    tmpIndex = largerIndex
                else:
                    break

    def createMinHeap(self, num):
        self.bigValueMinHeap.append(num)
        tmpIndex = len(self.bigValueMinHeap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if self.bigValueMinHeap[tmpIndex] < self.bigValueMinHeap[parentIndex]:
                self.bigValueMinHeap[parentIndex], self.bigValueMinHeap[tmpIndex] = \
                    self.bigValueMinHeap[tmpIndex], self.bigValueMinHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMinHeap(self, num):
        if num < self.bigValueMinHeap[0]:
            minHeapLen = len(self.bigValueMinHeap)
            self.bigValueMinHeap[0] = num
            tmpIndex = 0
            while tmpIndex < minHeapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                smallerIndex = 0
                #
                if rightIndex < minHeapLen:
                    smallerIndex = rightIndex if self.bigValueMinHeap[rightIndex] < self.bigValueMinHeap[leftIndex] else leftIndex
                elif leftIndex < minHeapLen:
                    smallerIndex = leftIndex
                else:
                    break
                #
                if self.bigValueMinHeap[smallerIndex] < self.bigValueMinHeap[index]:
                    self.bigValueMinHeap[smallerIndex], self.bigValueMinHeap[index] = \
                        self.bigValueMinHeap[index], self.bigValueMinHeap[smallerIndex]
                    index = smallerIndex
                else:
                    break

if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
        ans = s.GetMedian()
        print(ans)