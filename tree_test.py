class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. 深度优先
# 2. 广度优先

#对于深度优先来说：
#1. 先序遍历
#2. 中序遍历
#3. 后序遍历
# 注意；先序，中序，后序  都是对于根节点来说的，左、右节点都是先左后右

# 递归:
# 第一：找出口，怎么退出的？None返回空，退出

def PreOrderRecusive(root):#根节点-》左节点-》右节点
    if root == None:
        return None
    print(root.val)
    PreOrderRecusive(root.left)
    PreOrderRecusive(root.right)

def MidOrderRecusive(root):#左节点——》根节点——》右节点
    if root == None:
        return
    MidOrderRecusive(root.left)
    print(root.val)
    MidOrderRecusive(root.right)

def lastOrderRecusive(root):#左节点——》右节点——》根节点
    if root == None:
        return
    lastOrderRecusive(root.left)
    lastOrderRecusive(root.right)
    print(root.val)

#非递归的形式遍历树：先根，中根，后根
#递归，利用栈结构实现替代递归的操作
def preOrder(root):
    if root == None:
        return
    stack = []
    tmpNode = root #用来输出值
    while tmpNode or stack:
        while tmpNode:
            print(tmpNode.val)
            stack.append(tmpNode)#将根节点放到stack中
            tmpNode = tmpNode.left#遍历左节点
        node = stack.pop()#弹出左节点
        if node.right:
            tmpNode = node.right#遍历右节点
            #stack.append(node.right)

def MidOrder(root):
    if root == None:
        return
    stack = []
    tmpNode = root #用来输出值
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        print(node.val)
        if node.right:
            tmpNode = node.right

def BackForwordOrder(root):
    if root == None:
        return
    stack = []
    tmpNode = root #用来输出值
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left #遍历左子树，当tmpNode为空，即到了叶子节点，退出循环
        #node = stack.pop()
        node = stack[-1]#
        tmpNode = node.right#指针指向叶子节点stack里面的是叶子节点的根节点的根节点的右节点（叶子节点的右兄弟）
        if node.right == None:
            node = stack.pop()#如果叶子节点无右侧兄弟，则它的根节点弹栈，并打印
            print(node.val)
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.val)

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8
    print("PreOrderRecusive")
    PreOrderRecusive(t1)
    print("preOrder"+"==" * 30)
    preOrder(t1)
    print("MidOrderRecusive"+"==" * 30)
    MidOrderRecusive(t1)
    print("MidOrder"+"==" * 30)
    MidOrder(t1)
    print("lastOrderRecusive"+"==" * 30)
    lastOrderRecusive(t1)
    print("BackForwardOrder" + "==" * 30)
    BackForwordOrder(t1)