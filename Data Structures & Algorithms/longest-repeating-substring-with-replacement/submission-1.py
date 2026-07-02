class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        freq={}
        maxfreq=0
        for r in range(len(s)):
            c=s[r]
            freq[c]=freq.get(c,0)+1
            maxfreq= max(freq[c],maxfreq)
            while (r - l + 1) - maxfreq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        
            
        return res
