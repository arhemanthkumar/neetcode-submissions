class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        

        # If an array element = 'val'
        # Pop that element (num.pop())
        # Don't increment i now, because new element from right will occupy ith position.
        # Since the total elements reduced by 1, now reduce the len(nums) by 1.

        k = len(nums)

        if len(nums) == 0:
            return 0
        
        else:
            i = 0
            
            while (i < k):
                
                if nums[i] == val:
                    nums.pop(i)
                    k = k - 1
                    continue
                
                i += 1
        
        return k