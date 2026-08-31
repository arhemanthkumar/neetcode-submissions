class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False

        stack = []
        
        for bracket in s:

            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)

            elif stack:
            
                if bracket == ")" and stack[-1] == "(":
                    stack.pop()
                
                elif bracket == "}" and stack[-1] == "{":
                    stack.pop()
                
                elif bracket == "]" and stack[-1] == "[":
                    stack.pop()

                else:
                    stack.append(bracket)
            
            else:
                stack.append(bracket)

        
        if stack:
            return False

        return True
