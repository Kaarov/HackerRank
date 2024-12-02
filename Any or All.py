n = int(input())
numbers = list(map(int, input().split()))


def any_or_all(numbers):
    if all([True if i >= 0 else False for i in numbers]):
        if any([True if str(i) == str(i)[::-1] else False for i in numbers]):
            return True
    return False


print(any_or_all(numbers))

# Done ✅
