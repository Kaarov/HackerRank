
def swap_case(text):
    ans = ""
    for x in text:
        a = ord(x)
        if (a >= 97) and (a <= 122):
            ans += chr(a - 32)
        elif (a <= 90) and (a >= 65):
            ans += chr(a + 32)
        else:
            ans += x
    return ans


if __name__ == '__main__':
    if __name__ == '__main__':
        s = input()
        print(swap_case(s))

# Done ✅
