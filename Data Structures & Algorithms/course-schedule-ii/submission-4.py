class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {}

        for i in range(numCourses):
            preMap[i] = []

        for crs, pre in prerequisites:
        
            preMap[crs].append(pre)

        visitSet = set()
        cycle = set()

        res = []
        def dfs(course):

            if course in cycle:
                return False
            
            if course in visitSet:
                return True

            cycle.add(course)
            for pre in preMap[course]:

                if not dfs(pre):
                    return False
            cycle.remove(course)
            preMap[course] = []
            visitSet.add(course)
            res.append(course)
            return True

        for crs in range(numCourses):

            if not dfs(crs):
                return []

        return res

