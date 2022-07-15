class Node:
    def __init__(self,val,right=None,left=None):
        self.val=val
        self.right=right
        self.left=left
class Trees:
    def __init__(self):
        self.head=None
    def insertion(self,val):
        n=Node(val)
        itr=self.head
        if self.head==None:
            self.head=n
        else:
            i=0
            while i!=1:
                if itr.val>val:
                    if itr.left==None:
                        itr.left=n
                        i=1
                        print(f'{val} is inserted')
                    else:
                        itr=itr.left
                else:
                    if itr.right==None:
                        itr.right=n
                        i=1
                        print(f'{val} is inserted')
                    else:
                        itr=itr.right
    def search(self,data):
        itr=self.head
        while itr.val!=data:
            if itr!=None:
                print(itr.val)
            if itr.val>data:
                itr=itr.left
            else:
                itr=itr.right
            if itr==None:
                return None
        if itr!=None:
         print(f'{itr.val} is found')
    def deletion(self,data):
        if self.head==None:
             print('No node in tree')
             return 
        if self.head.left==None and self.head.right==None:
            if self.head.val==data:
                self.head=None
            return
        key_node=None
        q=[]
        q.append(self.head)
        temp=None
        while(len(q)):
            temp=q.pop(0)
            if temp.val==data:
                key_node=temp
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        if key_node:
            x=temp.val
            self.deletedeepest(temp)
            key_node.val=x
             
    def deletedeepest(self,d_node):
       q=[]
       q.append(self.head)
       while(len(q)):
            temp=q.pop(0)
            if temp is d_node:
               temp=None
               return
            if temp.right:
                if temp.right is d_node:
                    temp.right=None
                    return
                else:
                    q.append(temp.right)
                    
            if temp.left:
                if temp.left is d_node:
                    temp.left=None
                    return
                else:
                    q.append(temp.left)
    def delete_1(self,data):
        itr=self.head
        value='not found'
        while value=='not found':
           if itr!=None:
            if data<itr.val:
                itr=itr.left
            elif data>itr.val:
                itr=itr.right
            elif data==itr.val:
                value='found'
           else:
               if value=='not found':
                   print('value not found')
        
        itr1=self.head
        while itr1.right:
            itr1=itr1.right
            if itr1.right==None and itr1.left!=None:
                itr1=itr1.left
        print(itr1.val,itr.val)   
        itr.val=itr1.val
        self.deletedeepest(itr1)
    def inorder(self,head):
       itr=head
       res=[]
       if itr.left:
          res+=self.inorder(itr.left)
       res.append(itr.val)
       if itr.right:
         res+=self.inorder(itr.right)
       return res
    def preorder(self,head):
       itr=head
       res=[]
       res.append(itr.val)
       if itr.left:
          res+=self.inorder(itr.left)
       if itr.right:
         res+=self.inorder(itr.right)
       return res
    def postorder(self,head):
       itr=head
       res=[]
       if itr.left:
          res+=self.inorder(itr.left)
       if itr.right:
         res+=self.inorder(itr.right)
       res.append(itr.val)
       return res
    def post_in_pre(self):
        i=self.inorder(self.head)
        pre=self.preorder(self.head)
        n=pre[0]
        post=[]
        for j in i:
            if j!=n:
                post.append(j)
        post.append(pre[0])
        return post
        

if __name__ =='__main__':
    t1=Trees()
    t1.insertion(45)
    t1.insertion(47)
    t1.insertion(43)
    t1.insertion(53)
    t1.insertion(533)
    t1.insertion(32)
    t1.insertion(23)
    t1.insertion(44)
    t1.insertion(532)
    # t1.search(47)
    # t1.search(53)
   
   
    print('Inorder Traversal  ::',t1.inorder(t1.head))
    print('PreOrder Traversal ::',t1.preorder(t1.head))
    print('Postorder Traversal::',t1.postorder(t1.head)) 
    print('postorder from inorder and preorder',t1.post_in_pre())
    print('Inorder Traversal  ::',t1.inorder(t1.head))
    t1.delete_1(43)
    print('Inorder Traversal  ::',t1.inorder(t1.head))
    