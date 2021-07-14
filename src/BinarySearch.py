def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)
        guess = arr[mid]
        if num == guess:
            return mid
        if num < guess:
            high = high - 1
        else:
            low = low + 1
    return None


test = [1, 2, 3, 4, 5, 6]
print(binary_search(test, 4))
