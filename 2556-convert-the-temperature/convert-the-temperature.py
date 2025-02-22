class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        c=celsius
        k=c+273.15
        f=(c*1.80)+32
        return [k,f]