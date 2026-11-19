def duplicate(nums):
    d={}
    r={}
    new_list=[]
    maxi=0
    for i in nums:
        if i not in new_list:
            new_list.append(i)
            
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    freq=""        
    for key,value in d.items():
        if value>1:
            r[key]=value
    second_largest=float('inf')     
    for key,value in r.items():
        if value >maxi:
            second_largest=maxi
            maxi=value
        else:
            second_largest=None
                 
            
    return new_list,r ,second_largest   


numbers = [4, 2, 7, 4, 8, 2, 9, 7, 7, 3]
unique_list,duplicate_values,second_largest=duplicate(numbers)
print(f"""
unique_list:{unique_list},
duplicate_values:{duplicate_values},
second largest:{second_largest}""")