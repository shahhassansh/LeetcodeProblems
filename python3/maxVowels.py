class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        for i in range(k):
            if s[i] in "aeiou":
                cnt+=1
        mx_cnt = cnt
        for i in range(k,len(s)):
            if s[i-k] in "aeiou":
                cnt -=1
            if s[i] in "aeiou":
                cnt+=1
            mx_cnt = max(mx_cnt, cnt)
        return mx_cnt


        
