class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        store = {}

        for point in points:

            dist = self.distance(point)

            if dist in store:
                store[dist].append(point)
            else:
                store[dist] = [point]
        
        arr = list(store.keys())

        arr = sorted(arr)

        ctr = 0
        cur = 0
        result= []
        while ctr < k:

            key = arr[cur]
            
            ctr += len(store[key])
            result+= store[key]
            cur+=1
        
        return result
    

    def distance(self, point):

        dist = ((point[0])**2 + (point[1])**2)**(1/2)

        return dist
        
