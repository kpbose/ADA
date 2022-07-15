from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
         return self.container.append(val)
         
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        x=self.container[-1]
        print(x)
    def is_empty(self):
        x=(len(self.container)==0)
        print(x)
    def size(self):
        return len(self.container)
        
    def dis_stack(self):
        print(self.container)
class Queue:
    def __init__(self):
        self.container=deque()
    def push(self,val):
         return self.container.append(val)
         
    def pop(self):
        return self.container.popleft()
        
    def peek(self):
        x=self.container[-1]
        print(x)
    def is_empty(self):
        x=(len(self.container)==0)
        print(x)
    def size(self):
        return len(self.container)
        
    def dis_stack(self):
        print(self.container)
def reverse_string(s):
 s2=Stack()
 for char in s:
        s2.push(char)
 rev=''
 while s2.size()!=0:
     rev+=s2.pop()
 print(rev)
     
   
if __name__ =='__main__':
    s1=Queue()
    s1.push(7)
    s1.push(5)
    s1.push(3)
    s1.dis_stack()
    s1.pop()
    s1.push(78)
    s1.push(12)
    s1.dis_stack()
    s1.peek()
    s1.is_empty()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.pop()
    s1.push(8)
    s1.push(55)
    s1.push(65)
    s1.push(73)
    s1.size()
    s1.dis_stack()
    # s1=Stack()
    # s1.push(7)
    # s1.push(5)
    # s1.push(3)
    # s1.dis_stack()
    # s1.pop()
    # s1.push(78)
    # s1.push(12)
    # s1.dis_stack()
    # s1.peek()
    # s1.is_empty()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.pop()
    # s1.push(8)
    # s1.push(55)
    # s1.push(65)
    # s1.push(73)
    # s1.size()
    # s1.dis_stack()
    # reverse_string("We will conquere COVID-19")