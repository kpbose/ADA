from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        self.height=1
class AVL:
    def height(self,root):
        if root is None:
            return 0
        else:
            return root.height
    def balance(self,root):
        if root is None:
            return 0
        else:
            return self.height(root.left)-self.height(root.right)
    def Lrotation(self,root):
        a=root.right
        b=a.left
        a.left=root
        root.right=b
        root.height=1+max(self.height(root.left),self.height(root.right))
        a.height=1+max(self.height(a.left),self.height(a.right))
        return a
    def Rrotation(self,root):
        a=root.left
        b=a.right
        a.right=root
        root.left=b
        root.height=1+max(self.height(root.left),self.height(root.right))
        a.height=1+max(self.height(a.left),self.height(a.right))
        return a
    def insertion(self,val,root):
        if root is None:
            return Node(val)
        elif val<=root.val:
            root.left=self.insertion(val,root.left)
        elif val>root.val:
            root.right=self.insertion(val,root.right)
        root.height=1+max(self.height(root.left),self.height(root.right))
        balance=self.balance(root)
        if balance>1 and root.left.val>val:
            return self.Rrotation(root)
        if balance<-1 and root.right.val<val:
            return self.Lrotation(root)
        if balance>1 and root.left.val<val:
            root.left=self.Lrotation(root.left)
            return self.Rrotation(root)
        if balance<-1 and root.right.val>val:
            root.right=self.Rrotation(root.right)
            return self.Lrotation(root)
        return root
    def deletion_avl(self,root,val):
        if not root:
            print('No element to delete in avl tree')
            return root
        elif root.val>val:
            root.left=self.deletion_avl(root.left,val)
        elif root.val<val:
            root.right=self.deletion_avl(root.right,val)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.min_value(root.right)
            root.val=temp
            root.right=self.deletion_avl(root.right,temp)
        if root is None:
            return root
        root.height=1+max(self.height(root.left),self.height(root.right))
        balance=self.balance(root)
        if balance>1 and self.balance(root.left)>=0:
           return self.Rrotation(root)
        if balance<-1 and self.balance(root.right)<=0:
            return self.Lrotation(root)
        if balance>1 and self.balance(root.left)<0:
            root.left=self.Lrotation(root.left)
            return self.Rrotation(root)
        if balance<-1 and self.balance(root.right)>0:
            root.right=self.Rrotation(root.right)
            return self.Lrotation(root)
        return root
    def max_value(self,root):
        if root.right is None:
            return root.val 
        return self.max_value(root.right)
    def min_value(self,root):
        if root.left is None:
            return root.val 
        return self.min_value(root.left)   
    def preorder(self,root):
        if root is None:
            return
        res=[root.val]
        if root.left:
            res+=self.preorder(root.left)
        if root.right:
            res+=self.preorder(root.right)
        return res
    def inorder(self,root):
        if root is None:
            return
        res=[]
        if root.left:
            res+=self.inorder(root.left)
        res.append(root.val)
        if root.right:
            res+=self.inorder(root.right)
        return res
    def inorder_iterative(self,root):
        curr=root
        stack=deque()
        res=[]
        while stack or curr:
            if curr:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                res.append(curr.val)
                curr=curr.right
        print(res)
    def preorder_iterative(self,root):
        curr=root
        stack=deque()
        res=[]
        while stack or curr:
            if curr:
                stack.append(curr)
                res.append(curr.val)
                curr=curr.left
            else:
                curr=stack.pop()
                curr=curr.right
        print(res)
            
if __name__ =='__main__':
    a1=AVL()
    rt=None
    rt=a1.insertion(45,rt)
    rt=a1.insertion(67,rt)
    rt=a1.insertion(33,rt)
    rt=a1.insertion(12,rt)
    rt=a1.insertion(7,rt)
    rt=a1.insertion(9,rt)
    
    print(a1.preorder(rt))
    a1.preorder_iterative(rt)
    print(a1.inorder(rt))
    a1.inorder_iterative(rt)

    rt=a1.deletion_avl(rt,12)
    rt=a1.deletion_avl(rt,9 )
    a1.inorder_iterative(rt)