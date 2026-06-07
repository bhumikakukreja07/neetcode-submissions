class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        for first in s1:
            if first in hashmap1:
                hashmap1[first] += 1
            else:
                hashmap1[first] = 1

        left, right = 0, 0
        hashmap2 = {}

        for right in range(len(s2)):
            if s2[right] in hashmap2:
                hashmap2[s2[right]] += 1
            else:
                hashmap2[s2[right]] = 1

            while (right - left + 1) > len(s1):
                hashmap2[s2[left]] -= 1

                if hashmap2[s2[left]] == 0:
                    del hashmap2[s2[left]]
                left += 1
                
            if (right - left + 1) == len(s1):
                if hashmap1 == hashmap2:
                    return True
        return False