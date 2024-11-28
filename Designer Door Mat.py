# Enter your code here. Read input from STDIN. Print output to STDOUT

def header(n: int, m: int) -> str:
    ans = ""
    for i in range(n):
        center_text = ".|." * ((2 * i) + 1)
        length = (m - len(center_text)) // 2
        ans += "-" * length + center_text + "-" * length + "\n"
    return ans


def bottom(n: int, m: int) -> str:
    ans = ""
    for i in range(n - 1, -1, -1):
        center_text = ".|." * ((2 * i) + 1)
        length = (m - len(center_text)) // 2
        ans += "-" * length + center_text + "-" * length + "\n"
    return ans


def center(m: int) -> str:
    ans = "WELCOME"
    length = (m - len(ans)) // 2
    return "-" * length + ans + "-" * length + "\n"


def design_door_mat(n: int, m: int) -> str:
    upper_text = header(n // 2, m)
    center_text = center(m)
    bottom_text = bottom(n // 2, m)
    return upper_text + center_text + bottom_text


if __name__ == '__main__':
    n, m = map(int, input().split())
    result = design_door_mat(n, m)
    print(result)

# Done ✅
