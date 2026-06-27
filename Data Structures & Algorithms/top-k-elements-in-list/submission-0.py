class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap= {}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        pre_res = [[] for i in range(len(nums)+1)]
        res=[]
        for j in hmap:
            pre_res[hmap[j]].append(j)

        for m in range(len(pre_res)-1,0,-1):
            
            for n in pre_res[m]:
                res.append(n)
            if len(res)==k:
                return res
        
