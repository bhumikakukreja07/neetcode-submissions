class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {']':'[', ')':'(', '}':'{'}

        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                poppedCh = stack.pop()

                if poppedCh != hashmap[ch]:
                    return False
        if not stack:
            return True
        else:
            return False
        # return False