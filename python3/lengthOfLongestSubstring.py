class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        i, j = 0,1
        longest = 1
        e = set()
        e.add(s[i])
        while j < len(s):
            if s[j] in e:
                e.remove(s[i])
                i+=1
            else:
                e.add(s[j])
                j+=1
            longest = max(longest, j-i)
        return longest
