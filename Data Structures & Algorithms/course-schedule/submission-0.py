class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        state = [0] * numCourses
        def dfs(crs):
            if state[crs] == 1:
                return True
            if state[crs] == 2:
                return False
            
            state[crs] = 1
            
            for nei in adj[crs]:
                if dfs(nei): return True
            
            state[crs] = 2
            return False
        
        for course in range(numCourses):
            if state[course] == 0:
                if dfs(course): return False
        
        return True

        