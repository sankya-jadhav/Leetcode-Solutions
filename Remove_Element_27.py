class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst=[]
        for i in nums:
            if i != val:
                lst.append(i)
        nums[:] = lst
        k= len(nums)
        return k
    
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).