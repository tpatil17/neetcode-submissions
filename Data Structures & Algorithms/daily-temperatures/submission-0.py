class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []

        stack = []

        i = len(temperatures)-1

        while i >= 0:
            
            day_temp = temperatures[i]
            if i == len(temperatures)-1:
                result.append(0)
                stack.append([day_temp, i]) #record highest seen temp

            else:

                if day_temp < stack[-1][0]:
                    #found a high day
                    ind = stack[-1][1]
                    result.append(ind-i)
                    stack.append([day_temp, i])
                else:
                    # the current is bigger than any
                    while stack != []:
                        if stack[-1][0] <= day_temp:
                            stack.pop(-1)
                        else:
                            break
                    if stack == []:
                        result.append(0)
                    else:
                        ind = stack[-1][1]
                        result.append(ind-i)
                    stack.append([day_temp, i])
                        
            i-=1

        
 
        return result[::-1]
            




        