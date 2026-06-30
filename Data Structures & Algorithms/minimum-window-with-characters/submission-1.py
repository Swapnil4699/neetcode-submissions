class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == '':
            return ''
        res,reslen = [-1,-1], float('infinity')
        tcount, scount = {},{}
        for i in t:
            tcount[i] = tcount.get(i,0)+1
        have=0
        need =len(tcount)
        l = 0
        for r in range(len(s)):
            c = s[r]
            scount[c]= scount.get(c,0)+1
            if c in tcount and tcount[c] == scount[c]:
                have +=1

            while need == have:
                if (r-l+1)<reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                scount[s[l]] -= 1
            
                if s[l] in  tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float('infinity') else ''

                
        