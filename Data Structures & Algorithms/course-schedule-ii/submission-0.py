class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = { i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visitSet = [False] * numCourses
        stack = []
        done = set()

        def dfs(course):
            if visitSet[course]:
                return False  # loop
            if course in done:
                return True 
            
            visitSet[course] = True

            for pre in preMap[course]:
                if not dfs(pre): return False # check prerequisite of the courses

            visitSet[course] = False
            stack.append(course)
            done.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return []

        return stack