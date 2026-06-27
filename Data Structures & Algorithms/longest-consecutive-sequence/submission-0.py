class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup=set(nums)
        mx=0
        for i in range(len(nums)):
            if nums[i]-1 not in lookup:
                curr=nums[i]
                length=0
                while curr in nums:
                    curr+=1
                    length+=1
                mx= max(mx,length)
        return mx


