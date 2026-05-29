from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    n, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # build graph base on arr
    val_to_idx = {}
    for i, v in enumerate(arr):
        val_to_idx.setdefault(v, []).append(i)

    # init dist array
    dist = [-1] * n
    dist[0] = 0

    # init queue
    q = deque([0])

    process_val = set()

    # bfs
    while q:
        idx = q.popleft()
        if idx == n - 1:
            print(dist[idx])
            return
        # assign dist to current index
        d = dist[idx]

        # jump left/right
        for next_idx in [idx - 1, idx + 1]:
            if next_idx >= 0 and next_idx < n and dist[next_idx] == -1:
                dist[next_idx] = dist[idx] + 1
                q.append(next_idx)

        # teleport
        cur_val = arr[idx]
        if cur_val in process_val:
            continue

        process_val.add(cur_val)
        # target value index list
        for target_idx in (cur_val + K, cur_val - K):
            if target_idx in val_to_idx:
                for next_idx in val_to_idx[target_idx]:
                    if dist[next_idx] == -1:
                        dist[next_idx] = dist[idx] + 1
                        q.append(next_idx)
                
                # remove target value to avoid future process
                del val_to_idx[target_idx]
    
    print(dist[n-1])

if __name__ == "__main__":
    solve()
