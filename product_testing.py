# LG VHA's factory has a production line with N test machine. Each machine has its own working schedule [Ai, Bi], mean it start working from timestamp Ai and stop working after Bi. Example if machine schedule [1, 5] it can test product at timestamp 1, 2, 3, 4 and 5

# There are M products flowing in conveyor belt, product i enters line at timestamp Ti and leaves it Li timestamp later. One test machine can work in only one product a time (in particular, it is possible to test at the moment the product enters or leaves the line) and take 1 time unit to finish its testing. For example if product enter in time 2 and last 3 time unit, it can be tested at timestamp 2, 3, 4 or 5.

# Ms Hien Anh want to calculate what is the maximum number of products is tested?

# Input Format

# First line N and M number of test machine and number of products

# N next line contain 2 number Ai and Bi working schedule of i-th machine

# M next line contain 2 number Ti and Li timestamp when product i-th enter and existed time in line.

# Constraints

# 1 <= N <= 5

# 1 <= M <= 10^5

# 1 <= Ai, Bi, Ti, Li <= 10^8

import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().splitlines()
    
    # Read number of machines and products
    N, M = map(int, data[0].split())
    
    # Read machine schedules
    machines = []
    for i in range(1, N + 1):
        Ai, Bi = map(int, data[i].split())
        machines.append((Ai, Bi))
    
    # Read product schedules
    products = []
    for i in range(N + 1, N + M + 1):
        Ti, Li = map(int, data[i].split())
        products.append((Ti, Ti + Li - 1))  # Store as (start_time, end_time)
    
    # Sort machines by their start time
    machines.sort()
    
    # Sort products by their start time
    products.sort()
    
    # Create a list to keep track of available times for each machine
    available_times = [set(range(Ai, Bi + 1)) for Ai, Bi in machines]
    
    tested_count = 0
    
    for Ti, end_time in products:
        for i in range(N):
            # Check if the machine can test the product within its available times
            possible_times = available_times[i].intersection(set(range(Ti, end_time + 1)))
            if possible_times:
                # If there is a possible time to test the product
                tested_count += 1
                # Remove the used time from the machine's available times
                available_times[i].remove(min(possible_times))
                break  # Move to the next product after testing it
    
    print(tested_count)

if __name__ == "__main__":
    solve()