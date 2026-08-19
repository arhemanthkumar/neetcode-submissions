class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Approach 3: Two pointers / Sliding Window

        # Here, number 0 is our stop point.
        # Keep 2 pointers (i, j) which tracks the beginning and ending of contigous 1s.

        # Check if nums length has more than 1 element, if not, just return the only 1st element.
        if len(nums) > 1:
            nums.append(0)
            
            # Initializing counters
            i,j = 0, 0
            counter = 0


            while (j < len(nums)):
                if nums[j] == 1:
                    j = j + 1
                else:
                    counter = max(counter, j - i)
                    i = j + 1
                    j = j + 1
                    # Since i, j are pointing to same array element, if j points to 0, both i and j will be updated.
            
            return counter

        else:
            return nums[0]