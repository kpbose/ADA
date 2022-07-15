#single linked list
from platform import node


class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,val):
        n=Node(val,self.head)
        self.head=n        
    def insert_end(self,val):
        n=Node(val)
        if self.head==None:
           self.head=n
        else:
            itr=self.head
            while itr.next!=None:
                 itr=itr.next    
            itr.next=n
    def insert_values(self,datalist):
        for data in datalist:
            self.insert_end(data)
    def count_index(self):
        count=0
        itr=self.head
        while itr:
            count+=1 
            itr=itr.next
        print(f'length of the linked-list : {count} ')   
        return count
    def dis_index(self,ind):
        n=int(self.count_index())
        itr=self.head
        i=0
        for i in range (0,n):
            if i==ind:
               print(f'value at the index {ind} is : {itr.val}')
            itr=itr.next
            i+=1
    def rm_index(self,ind):
        if ind==0:
            self.head=self.head.next
        else:
         n=int(self.count_index())
         itr=self.head
         i=0
         while i!=ind-1:
            i+=1
            itr=itr.next
         print(f'value present on index no. {ind} is {itr.next.val} is being deleted')
         itr.next=itr.next.next
    def insert_after_value(self,data_after,data_to_insert):
        
        itr=self.head
        while itr.val !=data_after:
            itr=itr.next
        n=Node(data_to_insert,itr.next)
        itr.next=n
    def rem_by_value(self,data):
        if self.head==None:
            print('linked list is empty')
        elif self.head.val==data:
            self.head=self.head.next
        else:
         itr=self.head
         while itr.next.val!=data:
            itr=itr.next
         itr.next=itr.next.next
    def sort_insert(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
        elif data<self.head.val:
            self.insert_beginning(data)
        else:
            itr=self.head
            while itr!=None:
                if itr.next==None:
                 itr.next=n
                 return
                elif itr.next.val>data:
                 n.next=itr.next
                 itr.next=n
                 return
                itr=itr.next
    def reverse_ll(self):
        if self.head==None:
            print('Linked list empty')
            return
        if self.head.next==None:
            return  self.head
        itr=self.head
        prev=None
        while itr:
            next=itr.next
            itr.next=prev
            prev=itr
            itr=next
        self.head=prev
    def rec_rev_ll(self,head1):
        if head1==None:
            return head1
        if head1.next==None:
            return head1
        node1=self.rec_rev_ll(head1.next)
        head1.next.next=head1
        head1.next=None
        return node1

    def display(self):
     if self.head==None:
         print('linked list is empty')
     else:
      itr=self.head
      str1=''
      while itr:
        str1 +=str(itr.val) +'-->'
        itr=itr.next
      print(str1)
# l1=Linkedlist()
# l1.insert_beginning(4)
# l1.insert_beginning(25)
# l1.insert_beginning(55)
# l1.display()
# l1.insert_end(5)
# l1.display()
# l1.insert_beginning(75)
# l1.display()
# l1.insert_values(['mango','fruits'])
# l1.display()
# l1.count_index()
# l1.dis_index(2)
# l1.dis_index(0)
# l1.insert_end(78)
# l1.rm_index(4)
# l1.display()
# l1.insert_after_value(55,67)
# l1.display()
# l1.rem_by_value('mango')
# l1.display()

l2=Linkedlist()
l2.sort_insert(55)
l2.sort_insert(45)
l2.sort_insert(35)
l2.sort_insert(23)
l2.sort_insert(65)
l2.sort_insert(1)
l2.sort_insert(5)
l2.display()
l2.reverse_ll()
l2.display()
l2.head=l2.rec_rev_ll(l2.head)

l2.display()