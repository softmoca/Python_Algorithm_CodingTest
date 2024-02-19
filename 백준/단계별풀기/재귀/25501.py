def recursion(x,l,r):
    global cnt
    cnt+=1
    if l>=r:
        return [1,cnt]
    elif x[l]!=x[r]:
        return [0,cnt]
    else:
        
        return recursion(x,l+1,r-1)




def isPalindrome(x):
    return recursion(x,0,len(x)-1)


t=int(input())

for _ in range(t):
    
    cnt=0
    x,y=isPalindrome(input())
    print(x,y)
    
    




