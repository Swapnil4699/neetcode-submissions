class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        l=0
        res=0
        for r, val in enumerate(s):
            if val in seen:
                l = max(l,seen[val]+1)
            seen[val]=r
            res=max(res,r-l+1)
        return res
