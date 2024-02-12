


T=int(input())

for  _ in range(T):
    C=int(input())
    res=[0,0,0,0]
    res[0]+=C//25
    C=C%25
    res[1]+=C//10
    C=C%10
    res[2]+=C//5
    C=C%5
    res[3]=res[3]+C
    for x in res:
        print(x,end=' ')
    print()



        


