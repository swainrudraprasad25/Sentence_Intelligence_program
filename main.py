no_of_arr=int(input())
len_of_arr=int(input())
arr=input().split()
print(arr)
nums=[]
for i in arr:
    nums.append(int(i))
print(nums) 
#sort asc
n=len(nums)
for i in range(n-1):
    for j in range(n-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)            


for i in range(n-1):
    for j in range(n-1-i):
        if nums[j]<nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)            


 
