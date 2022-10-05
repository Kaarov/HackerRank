def count_substring(st, ss):
    count = 0

    for i in range(len(st)-len(ss)+1):
        if st[i:i+len(ss)] == ss:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))

# Done ✅
