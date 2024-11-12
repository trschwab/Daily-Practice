class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 == 1:
            return False

        stack = []
        
        complement = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for element in s:
            if element in complement.keys() and len(stack) == 0:
                return False
            elif element in complement.keys():
                if stack.pop() != complement[element]:
                    return False
            else:
                stack.append(element)

        if len(stack) == 0:
            return True
        return False
