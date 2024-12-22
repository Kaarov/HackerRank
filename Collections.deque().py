from collections import deque

ans = deque()

for _ in range(int(input())):
    i = input().split()
    if len(i) == 2:
        eval(f"ans.{i[0]}({i[1]})")
    else:
        eval(f"ans.{i[0]}()")

print(*ans)

# Done ✅
