# Check if pair with given Sum exists in Array
# Naive Approach 
"""" arr = list(map(int, input('enter some numbers : ').strip().split()))
l=len(arr)
i=0
x=4
found=False
while i < l:
    j=i+1
    while j < l:
        if arr[j]==x-arr[i]:
            print(j,'Yes')
            found=True
            break
        j+=1
    if found==True:
        break
    i+=1
if found==False:
    print('Not found') """

# In 0(NlogN)
def hasarraywithsun(arr,size,x):
    arr=sorted(arr)
    l=0
    r=size-1
    while l<r:
        if arr[l]+arr[r]==x:
            return 1
        elif arr[l]+arr[r]<x:
            l+=1
        else:
            r-=1
    return 0

arr=[2,3,4,5,6]
size=len(arr)
x=5
if hasarraywithsun(arr,size,x):
    print('Yes')
else:
    print('No')




