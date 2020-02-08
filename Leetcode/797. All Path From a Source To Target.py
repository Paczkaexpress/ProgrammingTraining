class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)

        def solve(node):
            if node == N-1: return [[N-1]]
            ans = []
            for nei in graph[node]:

                for path in solve(nei):
                    ans.append([node] + path)
            return ans

        return solve(0)