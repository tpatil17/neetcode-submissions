class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        pq = []

        heapq.heapify(pq) # priority que or max heap

        tasks_count = {}

        for i in tasks:

            if i in tasks_count:
                tasks_count[i]+=1
            else:
                tasks_count[i] = 1
            
        # tasks count contains a key value pair representing tasks and their fq

        order_tasks = [] # array representing the optimal order for tasks

        buffer = [] # store the task for n cycles before pushing back to pq

        for key, value in tasks_count.items():

            heapq.heappush(pq,(-value, key)) # max heap push
        
        #pq now contains a max heap with task and frequency

        # do while loop equivalent

        cycle_ct = 0 # count cycles

        count, task = heapq.heappop(pq) # pop the largest value to begin with

        count+=1

        buffer.append([(count, task), cycle_ct])

        order_tasks.append(task)

        while (len(pq) > 0) or (len(buffer) > 0):
        
            if len(buffer) > 0:

                if cycle_ct - buffer[0][1] == n: # wait complete
                    
                    pkg = buffer.pop(0) # pop the first val
                    
                    tpl = pkg[0] # the task fq tpl

                    heapq.heappush(pq, tpl)

            if len(pq) == 0:

                order_tasks.append("idl")
                cycle_ct +=1

            else:

                value, task = heapq.heappop(pq)

                if value == 0:

                    if len(buffer) == 0:

                        break # loop finished
                    else:
                        order_tasks.append("idl")
                        heapq.heappush(pq, (value, task))
                        cycle_ct+=1
                
                else:

                    value+=1
                    order_tasks.append(task)
                    cycle_ct += 1
                    buffer.append([(value, task), cycle_ct])
        
        # once the loop completes order_tasks is the len of the entire process

        return len(order_tasks) - n






        