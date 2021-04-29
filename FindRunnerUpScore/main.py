if __name__ == '__main__':
    n = int(input())
    # checkout note below explaining what the map() command does
    map_iterable = map(int, input().split())

    arr = list(map_iterable)
    arr.sort()

    maxNum = 0

    for x in arr:
        if x > maxNum:
            maxNum = x

    # Since the list is sorted, the first index is the lowest value in the list
    nextMax = arr[0]

    for i in arr:
        if i > nextMax and i != maxNum:
            nextMax = i

    print(nextMax)
