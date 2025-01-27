# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        sorted_arr=sorted(nums)
        length=len(nums)
        ans=[]
        for i in range(1, length+1):
            if i not in sorted_arr:
                ans.append(i)
        return ans
