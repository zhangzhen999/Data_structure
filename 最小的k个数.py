# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):

        #创建或者是插入最大堆
        def createMaxHeap(num):
            maxHeap.append(num)
            currentIndex = len(maxHeap) - 1
            while currentIndex != 0:
                parentIndex = (currentIndex - 1) >> 1
                if maxHeap[parentIndex] < maxHeap[currentIndex]:
                    maxHeap[parentIndex],maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
                else:
                    break
        #调整最大堆，实质上  头结点发生改变
        #case1：输入一个值和堆顶比较，
        #case2：在外面做好替换之后，我们做调整
        def adjustMaxHeap(num):
            if num < maxHeap[0]:
                maxHeap[0] = num
            # 用循环的方式来实现，也可以用递归
            maxHeapLen = len(maxHeap)
            index = 0
            while index < maxHeapLen:
                #左孩子和右孩子分别被计算
                leftIndex = index * 2 + 1
                rightIndex = index * 2 + 2
                largerIndex = 0
                #比较左孩子和右孩子哪个大？
                if rightIndex < maxHeapLen: #在比较之前，判断孩子节点是否超过堆的最大长度
                    if maxHeap[rightIndex] < maxHeap[leftIndex]:
                        largerIndex = leftIndex
                    else:
                        largerIndex = rightIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break
                #编程一般都用小于号< ,不用大于号 >
                if maxHeap[index] < maxHeap[largerIndex]: #index=0表示最大堆的堆顶，和他的孩子Node比较
                    maxHeap[largerIndex], maxHeap[index] = maxHeap[index] , maxHeap[largerIndex]
                index = largerIndex

        #开始执行找出最小的k个数
        maxHeap = []
        inputLen = len(tinput)
        if inputLen < k or k <= 0:
            return []

        for i in range(inputLen):
            if i < k:
                createMaxHeap(tinput[i])
            else:
                adjustMaxHeap(tinput[i])
        maxHeap.sort()
        return maxHeap
