class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.target = k
        self.stream = nums
        

    def add(self, val: int) -> int:

        self.stream.append(val)

        self.stream = sorted(self.stream)

        ind = len(self.stream)-self.target

        return self.stream[ind]
        
