class LRUCache:

    def __init__(self, capacity: int):

        self.cache = []
        self.store = {}
        self.cache_size = capacity
        

    def get(self, key: int) -> int:
        
        if key in self.store:
            for i in range(len(self.cache)):
                if self.cache[i] == key:
                    self.cache.pop(i)
                    break
            self.cache.append(key)
            return self.store[key]
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        
        if key in self.store:
            for i in range(len(self.cache)):
                if self.cache[i] == key:
                    self.cache.pop(i)
                    break
            self.cache.append(key)
            self.store[key] = value
        else:
            
            
            if len(self.cache) == self.cache_size:
                eject = self.cache.pop(0)
                
                del self.store[eject]
                
            self.store[key] = value
           
            self.cache.append(key)
            return
            


        
