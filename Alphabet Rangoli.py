def gen_line(nr, size):
    out = []
    for i in range(size, abs(nr), -1):
        out.append(i)
    out = out + out[:-1][::-1]
    ch = map(lambda x: chr(x + ord('a') - 1), out)
    return "-".join(ch)


def print_rangoli(size):
    ans = []
    for x in range(-size + 1, size):
        ans.append(gen_line(x, size))
    width = len(max(ans, key=len))
    for i in ans:
        print(i.center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
