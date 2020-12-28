from itertools import count
from itertools import cycle

for x in count(3, 1):
    if x > 10:
        break
    print(x)
count = 0

for item in cycle("121"):
    if count > 10:
        break
    print(item)
    count += 1
