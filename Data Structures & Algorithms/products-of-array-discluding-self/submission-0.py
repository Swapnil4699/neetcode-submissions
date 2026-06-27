class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s,p=1,1
        pans=[1]*len(nums)
        sans=[1]*len(nums)
        res=[]
        for i in range(len(nums)):
            pans[i]=p
            p=p*nums[i]
        for j in range(len(nums)-1,-1,-1):
            sans[j]=s
            s=s*nums[j]
        for k in range(len(nums)):
            ans=pans[k]*sans[k]
            res.append(ans)
        return res