s = 0
try:
    while True:
        for n in map(int, input().split()):
            s += n
        print(s)
except ValueError:
    print(s)
