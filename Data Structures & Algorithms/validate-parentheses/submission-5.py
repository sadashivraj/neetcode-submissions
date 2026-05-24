class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}': '{', ']':'[', ')':'('}
        openings = ('{', '[', '(')

        for i in s:
            if i in openings:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if pairs[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack


        