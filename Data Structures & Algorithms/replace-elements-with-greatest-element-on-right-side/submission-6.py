class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Suffix Sum - Optimised
        # TC: O(N), SC: O(1)

        currentMax = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = currentMax
            currentMax = max(currentMax, temp)

        return arr