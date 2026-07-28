class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        if len(nums) > 1:
            nums.append(0)
            
            i,j = 0, 0
            counter = 0

            while (j < len(nums)):
                if nums[j] == 1:
                    j = j + 1
                else:
                    counter = max(counter, j - i)
                    i = j + 1
                    j = j + 1
            
            return counter

        else:
            return nums[0]