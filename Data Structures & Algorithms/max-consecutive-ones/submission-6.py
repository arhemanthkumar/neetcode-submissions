class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Approach 1: Brute Force

        # TC: O(N^2), SC: O(1)

        # Keep outer loop at 1.
        # Run inner loop till 0 is met.
        # Count the 1's from inner loop count.

        n = len(nums)
        res = 0

        for i in range(n):
            count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                else:
                    count += 1

            res = max(res, count)

        return res