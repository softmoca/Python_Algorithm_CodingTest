def solution(nums):
    answer = 0
    for x in nums:
        x.append(1000)
        x.insert(0,1000)

    nums.append([1000,1000,1000,1000,1000,1000,1000])
    nums.insert(0,[1000,1000,1000,1000,1000,1000,1000])

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for i in range(1,6):
        for j in range(1,6):
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k]
                flag=0
                if nums[nx][ny]<=nums[i][j]:
                    flag=1
                    break
            else:
                answer+=1



    return answer
                       
print(solution([[10, 20, 50, 30, 20], [20, 30, 50, 70, 90], [10, 15, 25, 80, 35], [25, 35, 40, 55, 80], [30, 20, 35, 40, 90]]))
print(solution([[80, 25, 10, 65, 100], [20, 10, 32, 70, 33], [45, 10, 88, 9, 90], [10, 35, 10, 55, 66], [10, 84, 65, 88, 99]]))
print(solution([[33, 22, 55, 65, 55], [55, 88, 99, 12, 19], [18, 33, 25, 57, 77], [46, 78, 54, 55, 99], [33, 25, 47, 85, 17]]))

