def checkSubset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True


for i in range(int(input())):
    a = int(input())
    set_a = input().split()
    b = int(input())
    set_b = input().split()
    print(checkSubset(set_a, set_b))

# Done ✅
