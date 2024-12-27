class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dct = {}
        for x in prerequisites:
            if x[0] in dct:
                dct[x[0]].append(x[1])
            else:
                dct[x[0]] = [x[1]]
        taken = set()

        def dfs(c):
            if c not in dct or dct[c] == []:
                return True
            if c in taken:
                return False
            taken.add(c)
            for p in dct[c]:
                if dfs(p) == False:
                    return False
            dct[c] = []
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return False
        return True
