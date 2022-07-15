class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None
class Queue:
     ##Constructor function to make head of the list
    def __init__(self):
        self.head=None
     ##Function to push an element in the queue
    ##function to insert an element in the end of the list
    def push(self):
        val=input('Enter the element in stack')
        n=Node(val)
        if self.head==None:
            self.head=n
            self.head.next=n
        else:
            itr=self.head
            while itr.next!= self.head:
                itr=itr.next
            itr.next=n
            n.next=self.head
    ##Function to pop an element from the queue
    ##Function to delete an element from the end of the list
    def pop(self):
        itr=self.head
        if itr==None:
            print('No element to pop')
        elif self.head.next==self.head:
             print(self.head.val,' is deleted')
             self.head=None
        else:
            print(itr.val,' is deleted')
            self.head=itr.next
            itr1=self.head
            while itr1.next!=itr:
                itr1=itr1.next
            itr1.next=self.head
    ##Function to display queue
    def display(self):
        if self.head==None:
            print('queue is empty')
        else:
         itr=self.head
         str1=str(self.head.val)+'-->'
         itr=itr.next
         while itr!=self.head:
            str1+=str(itr.val)+'-->'
            itr=itr.next
         print(str1)
if __name__ =='__main__':
    q1=Queue()
    q1.push()
    q1.push()
    q1.push()
    q1.display()
    q1.pop()
    q1.pop()
    q1.pop()
    q1.display()