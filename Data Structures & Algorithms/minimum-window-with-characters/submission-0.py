class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}

        for i in t:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        left, right, count = 0, 0, 0
        window = {}
        valid = False
        ans = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in hashmap and window[char] == hashmap[char]:
                count += 1
            right += 1

            while left <= right and count == len(hashmap):
                char = s[left]

                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                window[char] -= 1

                if char in hashmap and window[char] < hashmap[char]:
                    count -= 1
                left += 1
        if ans[1] is not None:
            return s[ans[1]:ans[2]]
        else:
            return ""