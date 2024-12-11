from itertools import product


def get_product_itertools(list1: list[int], list2: list[int]) -> list[tuple[int, int]]:
    return list(product(list1, list2))


if __name__ == '__main__':
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(*get_product_itertools(list1, list2))
