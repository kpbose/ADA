class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Circular_LL:
    def __init__(self):
        self.head=None
    def insertbeg(self,val):
        n=Node(val)
        itr=self.head
        itr1=self.head
        if itr==None:
            self.head=n
            n.next=n
        else:
            itr=self.head
            itr1=self.head
            self.head=n
            n.next=itr
            while itr1.next!=itr:
                itr1=itr1.next
            itr1.next=n
    def insertend(self,val):
        itr=self.head
        itr1=self.head
        if itr==None:
            n=Node(val)
            self.head=n
            n.next=n
        else:
            n=Node(val,self.head)
            while itr.next!=self.head:
                itr=itr.next
            itr.next=n
    def delbeg(self):
        if self.head==None:
            print('Linked list empty')
        elif self.head.next==self.head:
            self.head=None
        else:
            itr=self.head
            self.head=self.head.next
            itr1=self.head
            while itr1.next!=itr:
                itr1=itr1.next
            itr1.next=self.head
    def delend(self):
        if self.head==None:
            print('Linked List Empty')
        elif self.head.next==self.head:
            self.head=None
        else:
            itr=self.head
            while itr.next.next!=self.head:
                itr=itr.next
            itr.next=self.head
    def insertpos(self,val,pos):
        n=Node(val)
        if self.head==None :
            self.head=n
            self.head.next=n
        elif pos==1:
            self.insertbeg(val)
        else:
            i=1
            itr=self.head
            while i!=pos-1:
                 itr=itr.next
                 i+=1
            if itr.next!=self.head and (self.cal_length())>=pos:
                itr1=itr.next
                itr.next=n
                n.next=itr1
            else:
                self.insertend(val)
    def cal_length(self):
        itr=self.head
        i=1
        while itr.next!=self.head:
            itr=itr.next
            i+=1
        return i
    def delet_kth(self,pos):
        n=self.cal_length()
        if self.head==None:
            print('Linked List empty')
            return
        if pos==1:
           self.delbeg()
           return
        if pos>=n:
          self.delend()
          return
        i=1
        itr=self.head
        while i!=pos-1:
            itr=itr.next
            i+=1
        itr.next=itr.next.next

    def display(self):
        if self.head==None:
            print('Linked list empty')
        else:
         itr=self.head
         str1=str(itr.val)+'-->'
         itr=itr.next
         while itr!=self.head:
             str1+=str(itr.val)+'-->'
             itr=itr.next
         print(str1)
if __name__ =='__main__':
 c1=Circular_LL()
 c1.insertbeg(28)
 c1.insertend(20)
 c1.insertbeg(45)
 c1.insertbeg(40)
 c1.insertbeg(34)
 c1.insertbeg(314)
 c1.insertend(41)
 c1.display()
 c1.delbeg()
 c1.delbeg()
 c1.display()
 c1.delend()
 c1.display()
 print(c1.cal_length())
 c1.insertpos(34,8)
 c1.display()
 c1.delet_kth(9)
c1.display()
