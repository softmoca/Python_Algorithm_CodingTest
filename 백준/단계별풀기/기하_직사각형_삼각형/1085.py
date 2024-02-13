x,y,w,h=map(int,input().split())


XX=min(abs(x-w),abs(y-h))

YY=min(x,y)

print(min(XX,YY))
