import sys
from collections import deque, defaultdict

def bfs(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    pattern_map = defaultdict(list)
    for word in wordList:
        for i in range(len(word)):
            pattern_map[word[:i] + "*" + word[i+1:]].append(word)

    queue = deque([(beginWord, 1)])
    visited = set([beginWord])
    while queue:
        word, level = queue.popleft()
        if word == endWord:
            return level
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i+1:]
            for next_word in pattern_map[pattern]:
                if next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, level + 1))
    return 0


def solve():
    data = iter(sys.stdin.read().split())
    beginWord = next(data)
    endWord = next(data)
    N = int(next(data))
    wordList = [next(data) for _ in range(N)]
    # sys.stdout.write(beginWord + "\n" + endWord + "\n")
    # sys.stdout.write(str(N) + "\n")
    # for word in wordList:
    #     sys.stdout.write(word + "\n")
    sys.stdout.write(str(bfs(beginWord, endWord, wordList)) + "\n")

if __name__ == "__main__":
    solve()