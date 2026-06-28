class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxprof = 0
        l,r=0,1
        while r<len(prices):
            prof=0
            if prices[r]>prices[l]:
                prof = prices[r]-prices[l]
                #l=r
            else:
                l=r
            r+=1
            mxprof = max(mxprof,prof)
        return mxprof
