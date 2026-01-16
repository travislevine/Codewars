def solution(nums):
    if nums is None:
        return []
    else:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j] # Swap
        return nums
print(solution([1,2,3,10,5]))
#You have passed all of the tests! :)
#https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/python