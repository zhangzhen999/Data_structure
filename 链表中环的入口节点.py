# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        #需要定义两个指针，一个快指针（两步），一个慢指针（一步）
        #循环跳
        #要么是快的指针为空（没有环），要么快慢相等（有环）
        if pHead == None:
            return None

        fastPointer = pHead
        slowPointer = pHead

        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break

        if fastPointer == None or fastPointer.next == None:
            return None #没有环

        #如果 slowPointer 走了 L 的长度，那么 fastPointer 就走了 2L 的长度
        #假设从开始到入口点的长度是 s，slowPointer 在环里面走的长度是 d
        #那么 L = s + d
        #假设环内 slowPointer 没走的长度是 m ，fastPointer 走的长度是多少
        # fastPointer 走的长度就是 n*(m + d) +d + s = 2L =2*(s + d)
        #化简上式得：s = m + (n-1)(m+d)
        fastPointer = pHead
        #让快慢指针在链表的入口节点相遇
        # 让循环链中的慢指针和从新从头结点出发的慢指针继续走，直至相遇（这里有一个条件，即s = m + (n-1)(m+d)），说明s和m差n-1圈，
        # 相遇应该在环链的起点，即他们会在在链表的入口节点相遇
        while fastPointer != slowPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next
        return fastPointer