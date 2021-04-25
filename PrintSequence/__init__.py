if __name__ == '__main__':
    n = int(input())

    num = 0
    for i in range(n+1):
        if i < 10:
            num = num * 10
            num = num + i
        elif i < 100:
            num = num * 100
            num = num + i
        else:
            num = num * 1000
            num = num + i


    print(num)