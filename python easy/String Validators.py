if __name__ == '__main__':
    s = input()

    isalnum = [i.isalnum() for i in s]
    isalpha = [i.isalpha() for i in s]
    isdigit = [i.isdigit() for i in s]
    islower = [i.islower() for i in s]
    isupper = [i.isupper() for i in s]

    print(any(isalnum))
    print(any(isalpha))
    print(any(isdigit))
    print(any(islower))
    print(any(isupper))

# Done ✅
