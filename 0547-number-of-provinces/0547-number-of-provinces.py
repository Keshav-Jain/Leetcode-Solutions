class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        province = 0

        for city in range(n):

            if visited[city]:
                continue
            province+=1
            stack=[city]
            while stack:
                current= stack.pop()
                if visited[current]:
                    continue
                visited[current]=True
                for neighbour in range(n):
                    if isConnected[current][neighbour] ==1 and not visited[neighbour]:
                        stack.append(neighbour)
        return province