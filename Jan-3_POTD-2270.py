from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Total sum of the array
        left_sum = 0  # Initialize running sum for the left part
        valid_splits = 0  # Counter for valid splits
        
        for i in range(len(nums) - 1):  # Iterate till the second last element
            left_sum += nums[i]  # Update left sum
            if left_sum >= total_sum - left_sum:  # Check if the split is valid
                valid_splits += 1
        
        return valid_splits