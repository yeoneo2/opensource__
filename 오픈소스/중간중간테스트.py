import numpy as np

def find_min(nums):
    min = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min

data = [8, 3, 5, 1, 9]

print("최솟값:", find_min)