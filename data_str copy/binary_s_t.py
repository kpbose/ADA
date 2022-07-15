class BinaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def insertion(self,val):
        if self.val>val:
                if self.left:
                    self.left.insertion(val)
                else:
                    self.left=BinaryTree(val)
        elif self.val<val:
                if self.right:
                    self.right.insertion(val)
                else:
                    self.right=BinaryTree(val)

    def inorder_traversal(self):
        res=[]
        if self.left:
          res+=self.left.inorder_traversal()
        res.append(self.val)
        if self.right:
         res+=self.right.inorder_traversal()
        return res
    def max_value(self):
        if self.right is None:
            return self.val 
        return self.right.max_value()
    def min_value(self):
        if self.left is None:
            return self.val 
        return self.left.min_value()
    def search(self,val):
        if self is None:
            return False
        if self.val==val:
            return True
        if self.val>val:
            if self.left:
                found=self.left.search(val)
                return found
        if self.val<val:
            if self.right:
                found=self.right.search(val)
                return found

    def deletion(self,key):
        found=self.search(key)
        if found:
            self.deletion_in_bst(key)
        else:
            print('value not found in bst')
            print('operation terminated')
        
    def deletion_in_bst(self,key):
        if self is None:
            print('BST is empty')
            return
        if self.val==key:
            if self.left==None and self.right==None:
               self.val=None
               return True
            if self.left!=None and self.right==None:
                self.val=self.left.val       
                self.right=self.left.right
                self.left=self.left.left
                return
            if self.left==None and self.right!=None:
                self.val=self.right.val
                self.left=self.right.left
                self.right=self.right.right
                return
            if self.left!=None and self.right!=None:
                value=self.left.max_value()
                self.deletion_in_bst(value)
                self.val=value
                return
        if self.val>key:
            if self.left:
                deleted=self.left.deletion_in_bst(key)
                if deleted:
                    self.left=None
        if self.val<key:
            if self.right:
               deleted=self.right.deletion_in_bst(key)
               if deleted:
                    self.right=None 
        
if __name__ =='__main__':
  b1=BinaryTree(43)
  b1.insertion(67)
  b1.insertion(6)
  b1.insertion(54)
  b1.insertion(39)
  b1.insertion(37)
  b1.insertion(41)
  b1.insertion(93)
  b1.insertion(77)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.deletion_in_bst(77)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.deletion_in_bst(93)
  b1.deletion_in_bst(6)
  b1.deletion_in_bst(67)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.deletion_in_bst(43)
  b1.deletion_in_bst(37)
  b1.deletion_in_bst(54)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.insertion(35)
  b1.insertion(55)
  b1.insertion(23)
  b1.insertion(37)
  b1.insertion(47)
  b1.insertion(60)
  b1.insertion(58)
  b1.insertion(59)
  b1.insertion(61)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.deletion_in_bst(60)
  print('Inorder Traversal::',b1.inorder_traversal())
  b1.deletion_in_bst(55)
  print('Inorder Traversal::',b1.inorder_traversal())
  print(b1.max_value(),'is max value')
  print(b1.min_value(),'is min value')
  b1.deletion(77)
  b1.deletion(37)
  print('Inorder Traversal::',b1.inorder_traversal())