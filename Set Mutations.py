"""
[1] .update() or |=
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

[2] .intersection_update() or &=
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])

[3] .difference_update() or -=
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])

[4] .symmetric_difference_update() or ^=
>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])
"""

_ = int(input())
ans = set(map(int, input().split()))
for _ in range(int(input())):
    oper, _ = input().split()
    match oper:
        case "update":
            ans |= set(map(int, input().split()))
        case "intersection_update":
            ans &= set(map(int, input().split()))
        case "difference_update":
            ans -= set(map(int, input().split()))
        case "symmetric_difference_update":
            ans ^= set(map(int, input().split()))
print(sum(ans))

# Done ✅
