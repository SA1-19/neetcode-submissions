class Solution:
    def isValid(self, s: str) -> bool:
        validity = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in validity:  
                stack.append(char)
            else:                  
                if not stack:
                    return False
                if validity[stack[-1]] != char:
                    return False
                stack.pop()

        return not stack