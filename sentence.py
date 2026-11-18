def frequency(nums):
    d={}
    for i in nums:
        if i !=" ":
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
    maxi=0
    freq=""
    for i,j in d.items():
        if j>maxi:
            maxi=j
            freq=i
    return freq         

def longest_sentence(nums):
    curr_word=""
    longest_word=""
    vowels=0
    consonant=0
    curr_length=0
    maxi=0
    word_count=0
    total_char=0
   
    for ch in nums:
        if ch !=" ":
            
            total_char+=1
            curr_word+=ch
            curr_length+=1
            if (ch=='a' or ch=='e' or ch=='o' or ch=='i' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'
            ):
                vowels+=1
            elif ('A'<=ch<='Z' or 'a'<=ch<='z'):
                consonant+=1
        else:
            if curr_length>0:
                word_count+=1
                if curr_length>maxi:
                    longest_word=curr_word
                    maxi=curr_length
                curr_word=""
                curr_length=0
    if curr_length>0:
        word_count+=1
        if curr_length>maxi:
            longest_word=curr_word
            maxi=curr_length            
    return  longest_word,word_count,vowels,consonant,total_char  
def reverse_in_order(nums):
    result=""
    curr_word=""
    for ch in nums:
        if ch !=" ":
            curr_word=ch+curr_word
        else:
            if curr_word!="":
                result+=curr_word+" "
            curr_word=""
    if curr_word!="":
        result+=curr_word+" "

    return result                                   

def sentence(words):
    longest_word,word_count,vowels,consonant,total_char=longest_sentence(words)
    char=frequency(words)
    result=reverse_in_order(words
    )
    print(f"""
    longest_word:{longest_word},
    vowels:{vowels},
    consonant:{consonant},
    total_words:{word_count},
    total_char:{total_char},
    frequent_char:{char},
    result:{result}""")
    
sentence(input("enter ur sentence:"))