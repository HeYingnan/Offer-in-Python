## 题目描述：请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.Mirror(pRoot, pRoot)

    def Mirror(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.Mirror(pRoot1.left, pRoot2.right) and self.Mirror(pRoot1.right, pRoot2.left)