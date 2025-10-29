import sys

def InputData():
	readl = sys.stdin.readline
	H, W = map(int, readl().split())
	A = [list(map(int, readl().split())) for _ in range(H)]
	N = int(readl())
	t = [list(map(int, readl().split())) for _ in range(N)]
	R, C = zip(*t)

	return H, W, A, N, R, C

dr = ( -1, 1, 0, 0, -1, -1, 1, 1 )
dc = ( 0, 0, -1, 1, -1, 1, -1, 1 )

def Touch(r, c):

	if A[r][c] == 0: V = 1
	else: V = 0
	A[r][c] = V

	for k in range(8):
		nr = r
		nc = c
		flag = False
		isboom = False

		while True:
			nr = nr + dr[k]
			nc = nc + dc[k]
			if nr < 0 or nr >= H or nc < 0 or nc >= W: break
			if A[nr][nc] == 2:
				isboom = True
			if A[nr][nc] == V:
				flag = True
				break
		if flag == True:
			if isboom == True:
				nr = r
				nc = c
				while True:
					nr = nr + dr[k]
					nc = nc + dc[k]
					if nr < 0 or nr >= H or nc < 0 or nc >= W: break
					A[nr][nc] = V
			else:
				nr = r
				nc = c
				while True:
					nr = nr + dr[k]
					nc = nc + dc[k]
					if A[nr][nc] == V:
						break
					A[nr][nc] = V

def Solve():
	cnt = 0
	for i in range(N):
		Touch(R[i], C[i])
	for i in range(H):
		for j in range(W):
			if A[i][j] == 1: cnt += 1
	return cnt

# 입력
# H: 격자의 세로길이 vertical length of grid
# W: 격자의 가로길이 horizontal length of grid
# A: 격자의 각 칸 each cell of the grid
# N: 터치 횟수 number of touches
# R: 터치하는 칸의 행번호 Line number of the cell you touch
# C: 터치하는 칸의 열번호 Column number of the cell you touch
H, W, A, N, R, C = InputData()

ans = -1
ans = Solve()

# 출력 Output
print(ans)