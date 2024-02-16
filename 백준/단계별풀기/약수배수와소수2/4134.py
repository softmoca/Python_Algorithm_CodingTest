x=int(input())


for _ in range(x):
    n=int(input())
    if n==1:
        print(2)
       
        continue
    if n==0:
        print(2)
    
        continue
    
    while True:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                n+=1
                break
        else:
            print(n)
            break




