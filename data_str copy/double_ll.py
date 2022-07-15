class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertBeg(self,val):
        n=Node(val,self.head)
        if self.head==None:
          self.head=n
        else:
           self.head.prev=n
           self.head=n
    def InsertEnd(self,val):
        n=Node(val)
        if self.head==None:
            self.InsertBeg(val)
        else:
            itr=self.head
            while itr.next!=None:
                itr=itr.next
            itr.next=n
            n.prev=itr
    def Traversal(self):
        if self.head==None:
            print('Linked list is empty')
        elif self.head.next==None:
            print('Linked list has only one node ',self.head.val)
        else:
          itr=self.head
          str1=''
          str2=''
          print('Traversal from beginning to end of the list')
          while itr.next!=None:
              str1 += str(itr.val)+ '-->'
              itr=itr.next
          str1 +=str(itr.val)+'-->'
          print(str1)
          itr2=itr
          print('Traversal from end to beginning of te list')
          while itr2!=None :
              str2 +=str(itr2.val)+'-->'
              itr2=itr2.prev
          print(str2)
    def Display(self):
        itr=self.head
        str1=' '
        while itr:
            str1 += str(itr.val)+ '-->'
            itr=itr.next
        print(str1)
    def del_beg(self):
        if self.head==None:
            print('Linked List is empty')
            return
        if self.head.next==None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
    def del_end(self):
        if self.head==None:
            print('Linked List is empty')
            return
        if self.head.next==None:
            self.head=None
            return
        itr=self.head
        while itr.next.next!=None:
            itr=itr.next
        itr.next.prev=None
        itr.next=None
    def cal_len(self):
        itr=self.head
        i=0
        while itr!=None:
            i+=1
            itr=itr.next
        return i
    def InsertPos(self,val,pos):
        n=Node(val)
        l=self.cal_len()
        if self.head==None:
            self.head=n
            return
        if pos==1:
            self.InsertBeg(val)
            return
        if pos>=l:
            self.InsertEnd(val)
            return
        i=1
        itr=self.head
        while pos-1!=i:
            itr=itr.next
        n.next=itr.next
        itr.next.prev=n
        n.prev=itr
        itr.next=n
    def delpos(self,pos):
        l=self.cal_len()
        if self.head==None:
            print('Linked list empty')
            return
        if self.head.next==None:
            self.head=None
            return
        if pos==1:
            self.del_beg()
            return
        if pos>=l:
            self.del_end()
            return
        i=1
        itr=self.head
        while i!=pos-1:
            itr=itr.next
            i+=1
        itr.next=itr.next.next
        itr.next.prev=itr
    def reverse(self):
        itr=self.head
        while itr.next!=None:
            itr=itr.next
        str1=''
        while itr!=None:
            str1+=str(itr.val)+'-->'
            itr=itr.prev
        print(str1)
if __name__ == '__main__':
    L1=LinkedList()
    L1.InsertBeg(45)
    L1.InsertBeg(40)
    L1.Display()
    L1.InsertEnd(68)
    L1.InsertEnd(75)
    L1.InsertEnd(15)
    L1.InsertEnd(345)
    L1.Display()
    L1.del_beg()
    L1.Display()
    L1.del_end()
    L1.Display()
    L1.InsertPos(43,4)
    L1.Display()
    L1.delpos(4)
    L1.Display()
    L1.reverse()