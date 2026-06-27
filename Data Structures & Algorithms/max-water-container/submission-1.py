class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        area=0
        while l<r:
            if heights[l]>heights[r]:
                p_ar = (r-l)*(min(heights[l],heights[r]))
                r-=1
            elif heights[l]<heights[r]:
                p_ar = (r-l)*(min(heights[r],heights[l]))
                l+=1
            else:
                p_ar = (r-l)*(heights[r])
                l+=1
                
            area=max(area,p_ar)
        return area