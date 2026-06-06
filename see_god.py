import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    # direction vectors: U, D, L, R
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dir_map = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        grid = [next(it).decode() for _ in range(n)]

        bad = [[False] * m for _ in range(n)]
        good_cnt = [[0] * m for _ in range(n)]
        rev = [[[] for _ in range(m)] for __ in range(n)]
        q = deque()

        # Initialisation
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                if c != '?':
                    d = dir_map[c]
                    ni = i + dx[d]
                    nj = j + dy[d]
                    if ni < 0 or ni >= n or nj < 0 or nj >= m:
                        bad[i][j] = True
                        q.append((i, j))
                    else:
                        rev[ni][nj].append((i, j))
                else:   # '?'
                    cnt = 0
                    for d in range(4):
                        ni = i + dx[d]
                        nj = j + dy[d]
                        if 0 <= ni < n and 0 <= nj < m:
                            cnt += 1
                    good_cnt[i][j] = cnt
                    if cnt == 0:
                        bad[i][j] = True
                        q.append((i, j))

        # BFS propagation
        while q:
            i, j = q.popleft()
            # fixed predecessors
            for pi, pj in rev[i][j]:
                if not bad[pi][pj]:
                    bad[pi][pj] = True
                    q.append((pi, pj))
            # neighbouring '?' cells
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '?' and not bad[ni][nj]:
                    good_cnt[ni][nj] -= 1
                    if good_cnt[ni][nj] == 0:
                        bad[ni][nj] = True
                        q.append((ni, nj))

        # Count cells that are NOT forced to exit (trapped)
        trapped = 0
        for i in range(n):
            for j in range(m):
                if not bad[i][j]:
                    trapped += 1
        out_lines.append(str(trapped))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()