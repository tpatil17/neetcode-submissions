class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == 0:
            return[]

        store = {}

        for i in range(len(nums)):

            if nums[i] not in store:
                store[nums[i]] = 1
            else:
                store[nums[i]] += 1
        
        result = list(store.items())

        result = sorted(result,key=lambda x: x[1])

        ans = []

        ctr = len(result)-1

        while k > 0:
            ans.append(result[ctr][0])
            ctr-=1
            k-=1
        
        return ans
        