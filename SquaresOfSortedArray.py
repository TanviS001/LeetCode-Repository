# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[]
        for i in nums:
            val=i*i
            sq.append(val)
        sorted_sq=sorted(sq)
        return sorted_sq
