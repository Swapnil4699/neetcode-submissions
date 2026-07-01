class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for k,v in enumerate(nums):
            c=target-v
            if c in hmap:
                return [hmap[c],k]

            hmap[v] = k
        