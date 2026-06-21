class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lngt=0
        l=0
        seen={}
        for r,val in enumerate(s):
            if val in seen:
                l=max(l,seen[val]+1)
            seen[val]=r
            lngt=max(lngt,r-l+1)
        return lngt