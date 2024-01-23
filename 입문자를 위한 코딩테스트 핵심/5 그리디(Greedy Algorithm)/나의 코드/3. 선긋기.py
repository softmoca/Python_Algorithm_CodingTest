def solution(m, nums):
    answer = 0
    nums.sort(key=lambda x:x[0])

    

    M=0
    for x in nums:
        if x[0]==0 and x[1]>M:
            M=x[1]
        elif x[0]>0:
            break

    for i in range (1,m+1):
        for j in range(i,M+1):
            if nums[i][1]>M




    return answer
    
                                           
print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
# print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
# print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
# print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
# print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))


