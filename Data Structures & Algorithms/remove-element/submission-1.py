class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = len(nums)

        if len(nums) == 0:
            return 0
        else:
            i = 0
            while (i < len(nums)):
                if nums[i] == val:
                    k -= 1
                    removed_element = nums.pop(i)
                    
                    continue
                i += 1
        return k