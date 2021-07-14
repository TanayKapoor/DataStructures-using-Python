def smallest_number(arr):
    smallest = arr[0]
    smallest_i = 0
    for i in range(1, len(len)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_i = i
    return smallest_i


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = smallest_number(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


test = [98, 45, 74, 10, 36, 58, 51, 20]
print(selection_sort(test))
