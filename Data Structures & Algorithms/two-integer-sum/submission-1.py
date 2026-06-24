class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i,v in enumerate(nums):
            req = target-v
            if req in dict:
                return [dict[req],i]
            dict[v]=i