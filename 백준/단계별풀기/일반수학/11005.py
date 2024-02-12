n,m=map(int,input().split())

stack=[]
while n>0:
    stack.append(n%m)
    n=n//m


for i in range(len(stack)):
    x=stack.pop()

    if 0<=x<10:
        print(x,end='')
    else:
        print(chr(x+55),end='')





