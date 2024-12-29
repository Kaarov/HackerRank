def check_superset(superset: set) -> bool:
    for _ in range(int(input())):
        new_set = set(map(int, input().split()))
        if len(new_set - superset) == 0:
            if len(new_set) == len(superset):
                return False
        else:
            return False
    return True


if __name__ == "__main__":
    superset = set(map(int, input().split()))
    print(check_superset(superset))

# Done ✅
