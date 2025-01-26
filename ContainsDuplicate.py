# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        unique=set(nums)
        unique_length=len(unique)
        if length==unique_length:
            return False
        else: 
            return True
