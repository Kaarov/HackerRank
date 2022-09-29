def split_and_join(text):
    a = list(text)
    for x in range(len(a)):
        if a[x] == ' ':
            a[x] = '-'
    return "".join(a)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Done ✅
