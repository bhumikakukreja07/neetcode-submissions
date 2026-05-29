class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        left = 0
        right = len(strs) - 1

        while left < right:
            if strs[right] != strs[left]:
                return False
            else:
                left += 1
                right -= 1
        return True