def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    arr.sort()
    if len(arr) > 0:
        head = 0
        tail = len(arr) - 1
        while head <= tail:
            mid = int((head + tail) / 2)
            if target == arr[mid]:
                return mid
            else:
                if target < arr[(mid)]:
                    tail = mid - 1
                else:
                    head = mid + 1

    return -1  # not found


print(binary_search([1, 2, 4, -5, -7, 8, 9], 8))
