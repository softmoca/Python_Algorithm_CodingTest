import sys
while True:
    arr=list(sys.stdin.readline())
    if arr[0]=='.':
        break
    
    stack=[]
    for x in arr:
        if x=='(':
            stack.append(x)
        elif x==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                print("no")
                break
        if x=='[':
            stack.append(x)
        elif x==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                print("no")
                break
    else:
        if stack:
            print("no")
        else:
            print("yes")        



