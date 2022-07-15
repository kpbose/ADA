import heapq
def insert(heap,val):
   heapq.heappush(heap,val)
def get_min(heap):
    return heap[0]
def parent(i):
    return (i-1)//2
def Lchild(i):
    return (2*i)+1
def Rchild(i):
    return (2*i)+2
def extract_min(heap):
    return heapq.heappop(heap)
def build_heap(heap):
    heapq.heapify(heap)
    return heap
def decrease(heap,new_val,i):
   heap[i]=new_val
   while (i!=0 and heap[parent(i)] > heap[i]):
       heap[i],heap[parent(i)]=(heap[parent(i)],heap[i])
def delet(heap,i):
    decrease(heap,-999,i)
    extract_min(heap)   
if __name__ =='__main__':
    heap=[]
    insert(heap,57)
    insert(heap,44)
    insert(heap,75)
    print(heap)
    print(get_min(heap))
    par=parent(2)
    print(heap[par])
    extract_min(heap)
    print(heap)
    heap1=[11,4,36,7,9,63,5,56]
    print(build_heap(heap1))
    decrease(heap1,3,2)
    print(heap1)
    delet(heap1,2)
    print(heap1)