def print_formatted(number):
    length = len(format(number, "b"))

    for i in range(1, number + 1):
        print(f"{str(i).rjust(length)} "
              f"{format(i, 'o').rjust(length)} "
              f"{format(i, 'x').upper().rjust(length)} "
              f"{format(i, 'b').rjust(length)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Done ✅
