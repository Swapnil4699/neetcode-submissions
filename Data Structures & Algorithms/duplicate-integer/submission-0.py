class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        for k in hmap:
            if hmap[k]>1:
                return True
        return False