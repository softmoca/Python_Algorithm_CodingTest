#  메모리 초과

# n=int(input())

# ch=[0]*(n//6+2)
# ch[0]=1
# for i in range(1,n//6+2):
#     ch[i]=ch[i-1]+i*6

# for i in range(len(ch)):
#     if ch[i]>=n:
#         print(i+1)
#         break

n = int(input())

num = 1
cnt = 1
while n > num :
    
    num += 6 * cnt 
    cnt += 1 
print(cnt)

