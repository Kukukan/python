import sys

def solution() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    B = [int(next(it)) for _ in range(N)]

    days = [(A[i], B[i], A[i] + B[i]) for i in range(N)]

    # sort by A + B in ascending order
    days.sort(key=lambda x: x[2])

    best_day = 0
    best_cost = 0

    # try each day as voucher
    for i in range(N):
        ai, bi, totali = days[i]
        if ai > M:
            continue    # if the voucher day is beyond the number of days we have, skip it

        money_spent = M - ai  # money spent on the voucher day
        cnt = 1
        total_cost = ai  # cost of the voucher day

        # Traverse the days after the voucher day
        for j in range(N):
            if j == i:
                continue  # skip the voucher day itself
            aj, bj, totalj = days[j]

            if money_spent >= totalj:
                money_spent -= totalj
                cnt += 1
                total_cost += totalj
            else:
                break  # can't afford this day, break the loop

        if cnt > best_day or (cnt == best_day and total_cost < best_cost):
            best_day = cnt
            best_cost = total_cost
    
    sys.stdout.write(f"{best_day} {best_cost}\n")

if __name__ == "__main__":
    solution()