# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # 第一个参数给比较短的那个链表的值
        # 第二个参数给比较长的那个链表的值
        # 第三个参数是比较短的那个链表头
        # 第四个参数是比较长的那个链表头
        def findEqual(shortPointer, longPointer, shortHead, longHead):
            k = 0
            # 寻找出链表长度之间的差值
            while longPointer:
                longPointer = longPointer.next
                k += 1
            # 先让长的链表走k步，这里让pTmp1先走k步
            shortPointer = shortHead
            longPointer = longHead
            for i in range(k):
                longPointer = longPointer.next

            while shortPointer != longPointer:
                shortPointer = shortPointer.next
                longPointer = longPointer.next
            return shortPointer

        # 首先定义两个临时指针
        pTmp1 = pHead1
        pTmp2 = pHead2
        # 其中一个走到最后，另一个
        while pTmp1 and pTmp2:
            if pTmp1 == pTmp2:
                return pTmp1
            # 指针移动
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next

        if pTmp1:
            return findEqual(pTmp2, pTmp1, pHead2, pHead1)
        if pTmp2:
            return findEqual(pTmp1, pTmp2, pHead1, pHead2)

if __name__  == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(7)
    c = ListNode(9)

    d = ListNode(2)
    e = ListNode(4)
    f = ListNode(7)
    g = ListNode(9)

    a.next = b
    b.next = c

    d.next = e
    e.next = f
    f.next = g


    node = s.FindFirstCommonNode(a,b)
    while node:
        print(node.val)
        node = node.next