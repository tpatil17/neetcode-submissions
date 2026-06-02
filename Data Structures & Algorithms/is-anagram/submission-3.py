class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        store = {}

        for i in s:
            if i not in store:
                store[i] =1
            else:
                store[i]+=1
        
        for j in t:
            if j not in store:
                return False
            else:
                store[j]-=1

        print(store.values())
        for i in store.values():
            if i != 0:
                return False
            

        
        return True
        