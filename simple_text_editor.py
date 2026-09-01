if __name__ == "__main__":
    q = int(input())
    stack = []
    s = str()
    for _ in range(q):
        operation = input().strip().split()
        ope = operation[0]
        if ope == "1":
            stack.append(s)
            s += operation[1]
        elif ope == "2":
            stack.append(s)
            s = s[:-int(operation[1])]
        elif ope == "3":
            print(s[int(operation[1])-1])
        elif ope == "4":
            s = stack.pop()