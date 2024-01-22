def solution(nums):
    n=len(nums)
    nums.insert(0,[1000]*(len(nums)))
    nums.append([1000]*(len(nums)-1))
    for x in nums:
        x.insert(0,1000)
        x.append(1000)

    answer = 0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(1,n+1):
        for j in range(1,n+1):
            flag=0
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                if  nums[i][j]>=nums[nx][ny]:
                    flag=1
                    break
            if flag==0:
              
                answer+=1


    

    return answer
                       
print(solution([[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
print(solution([[80, 25, 10, 65, 100], [20, 10, 32, 70, 33], [45, 10, 88, 9, 90], [10, 35, 10, 55, 66], [10, 84, 65, 88, 99]]))
print(solution([[33, 22, 55, 65, 55], [55, 88, 99, 12, 19], [18, 33, 25, 57, 77], [46, 78, 54, 55, 99], [33, 25, 47, 85, 17]]))

