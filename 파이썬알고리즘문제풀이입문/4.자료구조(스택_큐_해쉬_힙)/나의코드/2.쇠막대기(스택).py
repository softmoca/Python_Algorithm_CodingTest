arr=list(input())
cnt=0
stack=[]

for i in range(len(arr)):
    print(stack,cnt,arr[i])
    if arr[i]=='(':
        stack.append(arr[i])

    elif arr[i]==')':
        if arr[i-1]==')':
            stack.pop()
            cnt+=1
        elif arr[i-1]=='(':
            stack.pop()
            cnt+=len(stack)

print(cnt)







