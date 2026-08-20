class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Basic version - Un-Optimised
        # TC: O(N^2), SC: O(N)

        output = []

        for i in range(len(arr) - 1):
            right_element = arr[i+1:len(arr)]

            output.append(max(right_element))

        output.append(-1)

        return output