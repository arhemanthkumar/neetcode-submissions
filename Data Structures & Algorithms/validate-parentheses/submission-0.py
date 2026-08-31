class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        
        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
            
            elif bracket == ")" and stack[-1] == "(":
                stack.pop()
            
            elif bracket == "}" and stack[-1] == "{":
                stack.pop()
            
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            
            else:
                return False

        return True