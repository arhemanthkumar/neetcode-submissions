class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Approach 2: Iteration

        # If the element is 1, increase the count + 1.
        # If the element is 0, update the result with max (result, count).

        result = count = 0

        for num in nums:
            if num == 0:
                result = max(result, count)
                count = 0
            else:
                count += 1
        
        return max(count, result)