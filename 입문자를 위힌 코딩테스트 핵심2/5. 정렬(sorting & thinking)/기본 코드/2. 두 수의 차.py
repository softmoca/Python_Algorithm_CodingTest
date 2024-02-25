# def solution(nums):
#     answer = []
    
#     Minn=1000

#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if Minn>abs(nums[i]-nums[j]):
#                 Minn=abs(nums[i]-nums[j])

#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if Minn==abs(nums[i]-nums[j]):
#                 answer.append(sorted([nums[i],nums[j]]))
    

   
                
#     return answer

# print(solution([3, 8, 1, 5, 12]))
# print(solution([2, 1, 3, 5, 4]))
# print(solution([5, 10, 15, 20, 25, 11]))
# print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
# print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))


def solution(nums):
    answer = []
    nums.sort()
    Minn=1000

    for i in range(len(nums)-1):
        if Minn>abs( nums[i]-nums[i+1]):
            Minn=abs( nums[i]-nums[i+1])

    for i in range(len(nums)-1):
        if Minn==abs( nums[i]-nums[i+1]):
            answer.append([nums[i],nums[i+1]])
    
        
    
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
