# 시간 초과
# a,b,v=map(int,input().split())
# cnt=0
# while True:
#     cnt+=1
#     v=v-a
#     if v<=0:
#         print(cnt)
#         break
#     v=v+b
    

a, b, v = map(int, input().split())

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)




