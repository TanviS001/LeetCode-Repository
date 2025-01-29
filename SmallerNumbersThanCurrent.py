#1365. How Many Numbers Are Smaller Than the Current Number
# Approach 1:
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ret = []
        for i in range(0, length):
            count=0
            for j in range(length-1, -1, -1): 
                if nums[i]>nums[j]:
                    count=count+1
            ret.append(count)
        return ret 
        
# Learned Approach:

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        d={}
        for i, num in enumerate(temp):
            if num not in d:
                d[num]=i
        ret=[]
        for i in nums:
            ret.append(d[i])

        return ret
