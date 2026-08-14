class Solution:
    def reverseBits(self, n: int) -> int:

        binary = bin(n)[2:]

        rvrs = binary[::-1]

        while len(rvrs) < 32:
            rvrs+="0"
        
        return int(rvrs, 2)

        