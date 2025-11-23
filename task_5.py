# List Sorting (Custom) - asending and Descending

def custom_sort(arr, descending=False):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (descending and arr[j] < arr[j + 1]) or (not descending and arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example usage
print(custom_sort([64, 34, 25, 12, 22, 11, 90]))  # Should return sorted list in ascending order
print(custom_sort([64, 34, 25, 12, 22, 11, 90], descending=True))  # Should return sorted list in descending order


