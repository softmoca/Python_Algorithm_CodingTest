# def solution(nums, target):
#     answer = [0] * 2

#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 answer=[nums[i],nums[j]]
            

#     answer.sort()

#     return answer
        
                                       
# print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
# print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
# print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
# print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
# print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
# print(solution([7, 5, 12, 20], 15))






from collections import defaultdict
def solution(nums, target):
    answer = [0] * 2

    dic=defaultdict(int)

    for x in nums:
        y=target-x
        if y in dic:
            answer= sorted([x,y])
        dic[x]=1

    return answer
        
                                       
print(solution([7, 9, 2, 13, 3, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))