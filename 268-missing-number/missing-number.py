class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n3=set(nums)
        n=len(nums)

        n1=(n*(n+1)//2)
        n2=sum(nums)
        return(n1-n2)
