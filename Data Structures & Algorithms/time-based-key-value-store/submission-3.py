class TimeMap:

    def __init__(self):
        self.shelf = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.shelf:
            self.shelf[key] = [(value, timestamp)]
        else:
            self.shelf[key].append((value, timestamp))
        
        return
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.shelf:
            return ""
        else:
            arr = self.shelf[key]
            l = 0
            r = len(arr)-1

            if l == r:
                if timestamp >= arr[r][1]:
                    return arr[r][0]
                else:
                    return ""
            
            while l < r:

                mid = l+ (r-l)//2

                if arr[mid][1] > timestamp:
                    r = mid
                else:
                    l = mid + 1
            
            if arr[l][1] > timestamp:
                if l == 0:
                    return ""
                else:
                    return arr[l-1][0]
            else:
                return arr[l][0]

            
            
        

        
