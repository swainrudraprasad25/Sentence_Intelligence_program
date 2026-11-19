arr = [1, 2, 3, 5, 6, 3, 4, 6, 2]
arr.sort()
target=8
result=[]
n=len(arr)
for i in range(n-2):
    if i>0 and arr[i]==arr[i-1]:
        continue
    left=i+1
    right=n-1
    while left<right:
        curr_sum=arr[i]+arr[left]+arr[right]
        if curr_sum==target:
            result.append((arr[i], arr[left], arr[right]))
            left+=1
            right-=1
            while left<right and arr[left]==arr[left-1]:
                left+=1
            while left<right and arr[right]==arr[right+1]:  
                right-=1
        elif curr_sum<target:
            left+=1
        else:
            right-=1
print (result)                         
