cube = lambda x: x ** 3


def fibonacci(n):
    ans = [0, 1]
    for _ in range(2, n):
        ans.append(ans[-1] + ans[-2])
    return ans[:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# Done ✅
