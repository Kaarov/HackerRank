"""
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i

Result:
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
"""

from collections import defaultdict

ans = defaultdict(list)

n, m = map(int, input().split())

for _ in range(n):
    ans["A"].append(input())

for _ in range(m):
    ans["B"].append(input())

for b in ans["B"]:
    if b not in ans["A"]:
        print(-1)
    else:
        for a in range(n):
            if ans["A"][a] == b:
                print(a + 1, end=" ")
        print()

# Done ✅
