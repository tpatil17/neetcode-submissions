class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def dic_compare(d1,d2):
            if d1.keys() != d2.keys():
                return False
            
            for i in d1.keys():
                if d2[i] < d1[i]:
                    return False
            
            return True

        target = {}

        for i in t:
            target[i] = 1 + target.get(i, 0)
        
        # compare to the target

        store = {}

        l = 0
        r = 0
        string = []

        while r < len(s):
           
            if s[r] in target:
                store[s[r]] = 1 + store.get(s[r], 0)
            
            if dic_compare(target, store):

                while dic_compare(target, store):
                    if s[l] in store:
                        store[s[l]]-=1
                    l+=1
                
                l-=1
                store[s[l]]+=1

                if string == []:
                    string.append(s[l:r+1])
                else:
                    string[0] = s[l:r+1] if len(s[l:r+1]) <= len(string[0]) else string[0]
                
            
            r+=1
        
        if string == []:
            return ""
        else:
            return string[0]
            

        