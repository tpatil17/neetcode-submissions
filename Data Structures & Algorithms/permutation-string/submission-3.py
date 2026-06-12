class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        ws = len(s1)

        count = {}
        target = {}

        for i in s1:
            
            count[i] = 1+ count.get(i, 0)
        
        # count is the condition to be satisfied
        l = 0

        for i in range(len(s1)):

            if s2[i] not in count:
                l = i+1
                target = {}
                break
            else:
                target[s2[i]] = 1 + target.get(s2[i], 0)
        #compare if dictionaries match
        if target == count:
            return True
        
        r = l+ws-1 # window

        while r < len(s2):
            
            if target == {}: 
                for i in range(l, r+1):
                    if s2[i] in count:
                        target[s2[i]] = 1 + target.get(s2[i], 0)
                    else:
                        l = i+1
                        r = l+ws-1
                        target = {}
                        break
            else:
            
                if target == count:
                    return True
                else:

                    target[s2[l]] -= 1
                    l+=1
                    r+=1
                    if r == len(s2):
                        break

                    elif s2[r] not in count:
                        l = r+1
                        r = l + ws-1
                        target = {}
                        continue
                    
                    else:
                        target[s2[r]] = 1 + target.get(s2[r], 0)
        
        return False



        


        




        