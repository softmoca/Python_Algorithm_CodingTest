def fib_def(n):
    global cnt_dfs
    
    if n==1 or n==2:
        return 1
    else:
        cnt_dfs+=1
        return fib_def(n-1)+fib_def(n-2)

def fib_dp(n):
    global cnt_dp
    if dp[n]!=0:
        return dp[n]

    

    
    if n==1 or n==2:
        return 1
    else:
        cnt_dp+=1
        dp[n]= fib_dp(n-1)+fib_dp(n-2)
        return dp[n]
        
cnt_dfs=1
cnt_dp=0
n=int(input())

dp=[0]*(n+1)

fib_def(n)
fib_dp(n)

print(cnt_dfs,cnt_dp)





