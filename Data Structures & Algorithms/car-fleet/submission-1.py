class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(position[i],speed[i]) for i in range(len(speed))]

        new_pair = sorted(pair)

        new_pair = new_pair[::-1] # descending order by position

        fleets = []

        for pos, speed in new_pair:

            time = ((target)- pos)/speed

            if fleets == []:
                fleets.append(time)
            else:
                if fleets[-1] < time:
                    fleets.append(time)
        
        return len(fleets)
                


        