##Class for making a node
class Node:
    ##constructor function for making a node whose next is by default None
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
##Stack as linked list
##LIFO
##Insertion at end of the list
##Deletion at end of the list
class Stack:
    ##Constructor function to make head of the list
    def __init__(self):
        self.head=None
    ##Function to push an element in the stack
    ##function to insert an element in the end of the list
    def push(self):
        val=input('Enter in element in stack')
        n=Node(val)
        if self.head==None:
            self.head=n
        else:
            itr=self.head
            while itr.next!= None:
                itr=itr.next
            itr.next=n
    ##Function to pop an element from the stack
    ##Function to delete an element from the end of the list
    def pop(self):
        itr=self.head
        if itr==None:
            print('No element to pop')
        elif itr.next==None:
            print(itr.val,' is deleted')
            self.head=None
        else:
            while itr.next.next!=None:
                itr=itr.next
            print(itr.next.val,' is  deleted')
            itr.next=itr.next.next
    #Function to display stack
    def display(self):
        itr=self.head
        str1=' '
        while itr:
            str1+=itr.val+'-->'
            itr=itr.next
        print(str1)
##Queue as linked list
##FIFO
##Insertion at the end of  the list
##Deletion at the beginning of the list
class Queue:
     ##Constructor function to make head of the list
    def __init__(self):
        self.head=None
     ##Function to push an element in the queue
    ##function to insert an element in the end of the list
    def push(self):
        val=input('Enter in element in stack')
        n=Node(val)
        if self.head==None:
            self.head=n
        else:
            itr=self.head
            while itr.next!= None:
                itr=itr.next
            itr.next=n
    ##Function to pop an element from the queue
    ##Function to delete an element from the end of the list
    def pop(self):
        itr=self.head
        if itr==None:
            print('No element to pop')
        else:
            print(itr.val,' is deleted')
            self.head=itr.next
            itr=None
    ##Function to display queue
    def display(self):
        itr=self.head
        str1=' '
        while itr:
            str1+=itr.val+'-->'
            itr=itr.next
        print(str1)
##For implement Stack Just change the Class name from 
##Queue to Stack while creating the object
if __name__ =='__main__':
 s1=Queue()
 ch=0
 while ch!=4:
  print('Enter 1 to push')
  print('Enter 2 to pop')
  print('Enter 3 to display stack')
  print('Enter 4 for exit')
  ch=int(input('Enter your choice'))
  if ch==1:
     s1.push()
  elif ch==2:
     s1.pop()
  elif ch==3:
     s1.display()