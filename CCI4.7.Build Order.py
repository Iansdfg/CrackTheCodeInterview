class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited = [0]*numCourses
        path =[]
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for ele in graph[i]:
            if not self.dfs(graph, visited, ele, path):
                return False
        visited[i] = 2
        path.append(i)
        return True
