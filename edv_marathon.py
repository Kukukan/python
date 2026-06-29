import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    T = int(next(it))

    pos = []
    for _ in range(N):
        a = int(next(it))
        s = int(next(it))
        pos.append(a + s*T)
    
    # res = 0
    # cur_min = 10**18
    # for i in range(N -1, -1, -1):
    #     if pos[i] < cur_min:
    #         res += 1
    #         cur_min = pos[i]
    # sys.stdout.write(str(res))

    # monotic stack
    stack = []
    for i in range(N - 1, -1, -1):
        if not stack or pos[i] < stack[-1]:
            stack.append(pos[i])
    sys.stdout.write(str(len(stack)))

if __name__ == "__main__":
    solve()