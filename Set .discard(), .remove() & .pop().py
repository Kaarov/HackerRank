n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    oper = input().split()
    if len(oper) == 1:
        s.pop()
    else:
        eval(f"s.{oper[0]}({int(oper[1])})")

print(sum(s))

# Done ✅
