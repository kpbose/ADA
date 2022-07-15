def parent(i):
    return (i-1)//2
def Lchild(i):
    return (2*i)+1
def Rchild(i):
    return (2*i)+2
def insert_in_heap(heap_arr,val):
    heap_arr.append(val)
    i=len(heap_arr)-1
    while i!=0 and heap_arr[parent(i)]>heap_arr[i]:
         heap_arr[i],heap_arr[parent(i)]=(heap_arr[parent(i)],heap_arr[i])
         i=parent(i)
def heapify(arr):
    heap_arr=[]
    for val in arr:
        heap_arr.append(val)
        i=len(heap_arr)-1
        while i!=0 and heap_arr[parent(i)]>heap_arr[i]:
          heap_arr[i],heap_arr[parent(i)]=(heap_arr[parent(i)],heap_arr[i])
          i=parent(i)
    return heap_arr
def deletion(heap_arr,val):
    n=len(heap_arr)
    for i in range(0,n):
        if heap_arr[i]==val:
            j=i
    heap_arr[n-1],heap_arr[j]=(heap_arr[j],heap_arr[n-1])
    heap_arr.pop()
    l=Lchild(j)
    r=Rchild(j)
    while (l<n-2 or r<n-2) and (heap_arr[l]<heap_arr[j] or heap_arr[r]<heap_arr[j]):
        temp=j
        if heap_arr[l]<heap_arr[j]:
            temp=l
        if heap_arr[r]<heap_arr[l]:
            temp=r
        heap_arr[temp],heap_arr[j]=(heap_arr[j],heap_arr[temp])
        j=temp
        l=Lchild(j)
        r=Rchild(j)

    
         
if __name__ =='__main__':
    heap=[]
    insert_in_heap(heap,34)
    insert_in_heap(heap,21)
    insert_in_heap(heap,57)
    insert_in_heap(heap,7)
    print(heap)
    arr=[4,9,54,1,3]
    arr2=heapify(arr)
    insert_in_heap(arr2,61)
    insert_in_heap(arr2,57)
    insert_in_heap(arr2,11)
    print(arr2)
    deletion(arr2,3)
    deletion(arr2,54)
    deletion(arr2,61)
    deletion(arr2,1)
    print(arr2)