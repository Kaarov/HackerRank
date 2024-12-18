import re

for _ in range(int(input())):
    a = input()
    try:
        re.compile(a)
        print(True)
    except re.error:
        print(False)
