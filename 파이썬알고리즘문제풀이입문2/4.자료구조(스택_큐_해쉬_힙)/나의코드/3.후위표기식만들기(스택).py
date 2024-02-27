s=input()
stack=[]
answer=[]
for x in s:
    if x.isnumeric():
        answer.append(x)
    elif x=='(':
        stack.append(x)





    elif x==')':
        while stack and  stack[-1]!='(':
            answer.append(stack.pop())
            print(stack)
        
        stack.pop()
        
    elif x=='+' or x=='-':
        if stack:
            answer.append(stack.pop())
        stack.append(x)
    elif x=='*' or x=='/':
        if stack[-1]=='/'or stack[-1]=='*':
            answer.append(stack.pop())
        stack.append(x)

for x in answer:
    if x!='(':
        print(x,end='')














