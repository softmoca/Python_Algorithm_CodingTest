arr=input()
stack=[]

for x in arr:
    if x.isdecimal():
        stack.append(int(x))
    elif x =='+':
        stack.append(stack.pop() + stack.pop())
    elif x =='-':
        temp=stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(temp)
    elif x =='*':
        stack.append(stack.pop() * stack.pop())
    elif x =='/':
        temp=stack[-2] / stack[-1]
        stack.pop()
        stack.pop()
        stack.append(temp)
print(stack[0])

