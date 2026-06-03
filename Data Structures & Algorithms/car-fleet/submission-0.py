class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(position[i], speed[i])for i in range(len(speed))]

        pos_speed = sorted(pos_speed)[::-1]


        times = []

        for i in range(len(pos_speed)):

            if i == 0:
                pos, sp = pos_speed[i]
                times.append((target-pos)/sp)
                # position and time to dest
            else:
                pos, sp = pos_speed[i]

                time = (target-pos)/sp #time to destination

                if time > times[-1]:
                    times.append(time)
        
        return len(times)




        