if __name__ == '__main__':
    num_x = int(input())
    num_y = int(input())
    num_z = int(input())
    num_n = int(input())

    ans = []

    for x in range(num_x+1):
        for y in range(num_y+1):
            for z in range(num_z+1):
                result = []
                result.append(x)
                result.append(y)
                result.append(z)
                if x+y+z != num_n:
                    ans.append(result)
    print(ans)

# Done ✅
