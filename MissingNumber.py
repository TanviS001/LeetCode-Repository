# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_nums=sorted(nums)
        length=len(nums)
        for i in range(length+1):
            if i not in nums:
                return i
            
