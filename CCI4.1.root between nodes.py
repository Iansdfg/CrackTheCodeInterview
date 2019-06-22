class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(graph, 0, [0],res)
        return res

    def dfs(self, graph, pos, path, res):
        if pos == 3:
            res.append(path)
            return
        for ele in graph[pos]:
            self.dfs(graph, ele, path+[ele], res)



def execute():
    graph = [[1,2], [3], [3], []]
    sol = Solution()
    print(sol.allPathsSourceTarget(graph))

if __name__ == '__main__':
    execute()

