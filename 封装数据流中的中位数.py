# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        #大数放到小堆里，小数放到大堆里
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        def cmpMaxHeap(a, b):
            return a > b
        def cmpMinHeap(a, b):
            return a < b
        #有两种case：1是最大堆的节点数>最小堆的，case2：最大堆数= 最小堆数
        if self.maxHeapCount > self.minHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
                self.createHeap(tmpNum, self.bigValueMinHeap, cmpMinHeap)
            else:
                self.createHeap(num, self.bigValueMinHeap,cmpMinHeap)
        else:
            self.maxHeapCount += 1
            if len(self.littleValueMaxHeap) == 0:
                self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustHeap(num, self.bigValueMinHeap, cmpMaxHeap)
                    self.createHeap(tmpNum, self.littleValueMaxHeap, cmpMaxHeap)
                else:
                    self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
        #print(self.littleValueMaxHeap)
        #print(self.bigValueMinHeap)


    def GetMedian(self, n = None):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return float(self.littleValueMaxHeap[0] + self.bigValueMinHeap[0]) / 2

    #堆插入的函数
    def createHeap(self, num, heap, cmpfun):
        heap.append(num)
        tmpIndex = len(heap) - 1  #找出最大堆中最后的一个数给定一个索引 index
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if cmpfun(heap[tmpIndex] , heap[parentIndex]):
                heap[parentIndex], heap[tmpIndex] = \
                    heap[tmpIndex], heap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustHeap(self, num, heap, cmpFunc):
        if num < heap[0]:
            maxHeapLen = len(heap)
            heap[0] = num
            tmpIndex = 0
            while tmpIndex < maxHeapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                largerIndex = 0
                if rightIndex < maxHeapLen:
                    largerIndex = rightIndex if cmpFunc(heap[rightIndex], heap[leftIndex]) else leftIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break

                if cmpFunc(heap[largerIndex] , heap[tmpIndex]):
                    heap[largerIndex], heap[tmpIndex] = heap[tmpIndex], heap[largerIndex]
                    tmpIndex = largerIndex
                else:
                    break


if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
        ans = s.GetMedian()
        print(ans)