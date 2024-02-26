n=int(input())

for k in range(1,n+1):
    s=input()
    s=s.upper()
 
    for i in range(len(s)//2):
        if s[i]==s[-1-i]:
            
            continue
        else:
            print(f'#{k} NO')
            break
    else:
        print(f'#{k} YES')

