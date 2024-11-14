class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        brackDict = {
            '}':'{',
            ')':'(',
            ']':'['
            
        }
        for brack in s:
            if brack in brackDict:
                if stack and stack[-1] == brackDict[brack]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)
        if stack:
            return False
        return True