class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        res = []        # stores valid topological order
        visit = set()   # current recursion stack (cycle detection)
        done = set()    # fully processed courses

        def dfs(crs):
            if crs in visit:    # cycle detected
                return False
            if crs in done:     # already processed
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            done.add(crs)
            res.append(crs)     # append after all prereqs are done
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []       # cycle → impossible

        return res              # note: reverse is NOT needed