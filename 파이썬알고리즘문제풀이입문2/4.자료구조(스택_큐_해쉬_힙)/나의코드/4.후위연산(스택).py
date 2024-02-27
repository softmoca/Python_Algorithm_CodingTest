


arr=list(input())


# for i in range(len(arr)):
#     if arr[i].isnumeric():
#         arr[i]=int(arr[i])


stack=[]
for x in arr:
    if x.isnumeric():
        stack.append(int(x))
    else:
        a=stack.pop()
        b=stack.pop()
        if x=='+':
            stack.append(a+b)
     
        elif x=='-':
            stack.append(b-a)

        elif x=='/':
            stack.append(b//a)

        elif x=='*':
            stack.append(b*a)


print(stack[0])
