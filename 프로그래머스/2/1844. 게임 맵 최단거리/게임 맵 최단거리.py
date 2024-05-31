from collections import deque

def solution(maps):
    # 상하좌우 네 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 맵의 크기
    n = len(maps)
    m = len(maps[0])
    
    # BFS를 위한 큐 초기화
    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 목표 지점에 도달했는지 확인
        if x == n - 1 and y == m - 1:
            return distance
        
        # 네 방향으로 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵의 범위를 벗어나지 않고, 방문하지 않았으며, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    # 목표 지점에 도달할 수 없는 경우
    return -1