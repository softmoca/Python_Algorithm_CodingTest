arr=input()
res=[]
stack=[]

for x in arr:
    if x.isdecimal():
        res.append(x)
    elif x == '+' or x == '-':
        if stack and stack[-1]!='(':   
            res.append(stack.pop())
        stack.append(x)
    elif x == '*' or x =='/':
        if stack  :
            if stack[-1]=='*' or stack[-1]=='/':
                res.append(stack.pop())
        stack.append(x)
    elif x=='(':
        stack.append(x)
    elif x==')':
        while True:
            if stack[-1] =='(':
                stack.pop()
                break
            else:
                res.append(stack.pop())

while stack:
    res.append(stack.pop())

answer=''.join(map(str,res))
print(answer)


