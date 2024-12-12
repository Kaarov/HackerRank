from collections import Counter


def get_total_money(shoe_sizes: list[int]) -> int:
    ans = 0
    counter = Counter(shoe_sizes)
    for _ in range(int(input())):
        shoe, price = map(int, input().split())
        if counter[shoe] < 1:
            continue
        counter[shoe] -= 1
        ans += price
    return ans


if __name__ == "__main__":
    _ = int(input())
    shoe_sizes = list(map(int, input().split()))
    print(get_total_money(shoe_sizes))

# Done ✅
