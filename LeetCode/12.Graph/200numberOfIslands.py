import collections;

class Solution:
    def BFS(self, deq, dirs, limit_y, limit_x, grid , visited, answer):
        while len(deq):
            y, x = deq.popleft();
            for dir in dirs:
                ny = y + dir[0];
                nx = x + dir[1];
                if 0 <= nx < limit_x and 0 <= ny < limit_y and visited[ny][nx] == 0 and grid[ny][nx] == '1':
                    deq.append((ny, nx));
                    visited[ny][nx] = 1;
    
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        answer = 0;
        deq = collections.deque();
        
        visited = [[0] * len(grid[0]) for _ in range(len(grid))];

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1' and visited[y][x] == 0:
                    deq.append((y, x));
                    visited[y][x] = 1;
                    self.BFS(deq, dirs, len(grid), len(grid[0]), grid, visited, answer);
                    answer += 1;
                    
        return answer;
        