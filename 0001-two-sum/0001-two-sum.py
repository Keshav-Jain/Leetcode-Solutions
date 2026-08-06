class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        seen={}
        for i in range(0,n):
            comm=target-nums[i]
            if comm in seen:
                return [seen[comm],i]
            else:
                seen[nums[i]]=i


        
        