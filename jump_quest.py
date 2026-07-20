import sys

def solve() -> None:
    it = iter(sys.stdin.buffer.read().split())
    N = int(next(it))
    S = int(next(it))
    tiles = [(int(next(it)), int(next(it))) for _ in range(N)]

    typ = [0] * (N + 1)
    val = [0] * (N + 1)
    for i, (t, v) in enumerate(tiles, start=1):
        typ[i] = t
        val[i] = v

    pos = S
    direction = 1
    strength = 1
    destroyed = 0

    if typ[pos] == 1:
        if strength >= val[pos]:
            destroyed += 1
            val[pos] = -1
    else:
        strength += val[pos]
        direction = -direction

    visited = set()
    while 1 <= pos <= N:
        if strength <= N:
            state = (pos, direction, strength)
            if state in visited:
                break
            visited.add(state)

        nxt = pos + direction * strength
        if nxt < 1 or nxt > N:
            break
        pos = nxt

        if typ[pos] == 1:
            if val[pos] != -1 and strength >= val[pos]:
                destroyed += 1
                val[pos] = -1
        else:
            strength += val[pos]
            direction = -direction

    print(destroyed)

if __name__ == "__main__":
    solve()