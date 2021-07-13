def binary_search(iplist, number):
    low = 0
    high = len(iplist) - 1

    while low <= high:
        mid = (low + high)
        guess = iplist[mid]
        if guess == number:
            return mid
        if guess > number:
            high = high - 1
        else:
            low = low + 1
    return None


my_list = [2, 4, 6, 8, 10]
print(binary_search(my_list, 6))
print(binary_search(my_list, 1))
