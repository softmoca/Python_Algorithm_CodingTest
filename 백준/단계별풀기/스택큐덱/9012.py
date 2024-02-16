n=int(input())


for i in range(n):
    arr=list(input())
    stack=[]
   
    for x in arr:
        if x=='(':
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                Flag=1
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")


