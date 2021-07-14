def find_smallest(arr):
    smallest_num = arr[0]
    smallest_num_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_num_index = i
    return smallest_num_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


test_Arr = [65, 45, 12, 65, 2, 3, 78, 12, 46, 96, 13]
print(selection_sort(test_Arr))
