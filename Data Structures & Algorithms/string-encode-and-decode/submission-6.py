class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        end = "<end>"
        for i in strs:
            s+=i
            s+= end
        
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        return s.split("<end>")[:-1]
