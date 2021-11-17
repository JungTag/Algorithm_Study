def dfs(cur, cnt):
    visited[cur] = 1
    cnt += 1
    for adj in g[cur]:
        if not visited[adj]:
            cnt = dfs(adj, cnt)
    return cnt   

def dfs(y, x, cnt):
    visited[y][x] = 1
    cnt += 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if g[ny][nx] and not visited[ny][nx]:
                cnt = dfs(ny, nx, cnt)
    return cnt