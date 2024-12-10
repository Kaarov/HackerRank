from collections import Counter

k = int(input())
room_no = list(map(int, input().split()))

room_count = Counter(room_no)

for keys, values in room_count.items():
    if values < 5:
        print(keys)

# Done ✅
