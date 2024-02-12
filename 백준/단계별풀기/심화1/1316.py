n=int(input())
cnt=0
for _ in range(n):
    arr=list(map(str,input()))
    stack=[]

    for i in range(len(arr)):
        if stack:
            if (arr[i] in stack) and  stack[-1]!=arr[i]:
                    break
        stack.append(arr[i])
    else:
        cnt+=1
print(cnt)



    





