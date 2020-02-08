class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = set()
        maxCount = 0
        i = 0
        j = 0
        while(j < len(s) and i < len(s)):
            if(s[j] not in arr):
                arr.add(s[j])
                j += 1
                maxCount = max(maxCount, j - i)
            else:
                arr.remove(s[i])
                i += 1
        return maxCount