class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            result.append(self.binSum(bin(i)))
        
        return result

    def binSum(self , binary):

        ans = 0

        for i in binary[2:]:
            ans+=int(i)
        
        return ans
        