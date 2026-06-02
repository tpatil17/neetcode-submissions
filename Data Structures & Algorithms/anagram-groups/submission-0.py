class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        store = {}

        for word in strs:
            s_word = sorted(word)
            s_word = "".join(s_word)
            if s_word in store:
                store[s_word].append(word)
            else:
                store[s_word] = [word]
        
        return list(store.values())