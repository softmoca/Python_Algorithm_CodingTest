


s=input()

stack=[]
answer=0
for x in s:
    if x=='(':
        stack.append(x)
    elif x==')':
        if stack[-1]=='(':
            stack.pop()
            answer=answer+len(stack)
        elif stack[-1]==')':
            answer+=1
            stack.pop()
    print(x,stack,answer)

print(answer)










