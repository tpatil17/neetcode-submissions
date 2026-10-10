class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ans = []

        store = {}

        for i in range(len(s)):
            store[s[i]] = i
        
        end = 0
        count = 0

        for i in range(len(s)):
            count+=1
     
            if store[s[i]] > end:
                end = store[s[i]]
                

            if i == end:
                
                ans.append(count)
                count = 0
        
        return ans


                    