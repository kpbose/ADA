def binary_search(l,val):
    if val in l:
     n=len(l)
     print('current searching is in::',l)
     if val==l[n//2]:
        print(f'value is found ')
        return
     elif val<l[n//2]:
        l2=l[:n//2]
        binary_search(l2,val)
        return
     elif val>l[n//2]:
        l2=l[n//2:]
        binary_search(l2,val)
        return
    else:
        print('value not found')
def linear_search(l,val):
    if val in l:
        print('value is found')
    else:
        print('value not found')
l1=[]
n=int(input('Enter the size of array'))
print('Enter the elements in array')
i=0
while i!=n:
    l1.append(int(input()))
    i+=1
l1.sort()
binary_search(l1,6)
# linear_search(l1,7)