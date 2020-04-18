# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        #前序（根-左-右）：
        #中序（左-根-右）：
        if not pre or not tin:
            return
        if len(pre) != len(tin):
            return

        #取出pre的值
        root = pre[0]
        rootNode = TreeNode(root)#新建节点

        #在tin中找到root的pos
        pos = tin.index(root)

        #对中序切分
        tinLeft = tin[:pos]
        tinRight = tin[pos+1:]

        #对前序切片
        preLeft = pre[1:pos+1]
        preRight = pre[pos+1:]

        leftNode = self.reConstructBinaryTree(preLeft, tinLeft)
        rightNode = self.reConstructBinaryTree(preRight, tinRight)

        if leftNode:
            rootNode.left = leftNode
        if rightNode:
            rootNode.right = rightNode
        return rootNode

if __name__ == '__main__':
    s = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    ans = s.reConstructBinaryTree(pre, tin)
    print(ans.val)
    print(ans.left.val)
    print(ans.right.val)
    print(ans.left.left.val)
    #print(ans.left.right.val)
    print(ans.right.left.val)