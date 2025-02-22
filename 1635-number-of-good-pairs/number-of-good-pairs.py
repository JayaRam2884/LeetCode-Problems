class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=0
        for i in d:
            if d[i]>=2:
                res+=(d[i]-1)*(d[i])//2
        return res

        