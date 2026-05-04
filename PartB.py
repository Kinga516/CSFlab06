def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Task 3: Selection Sort
original = [64, 25, 12, 22, 11]
print("Original List:", original)
sorted_list = selection_sort(original.copy())
print("Sorted List:", sorted_list)

print()  

# Task 4: Trace Selection Sort
def selection_sort_with_trace(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Pass {i+1}: {arr}")
    return arr

original2 = [64, 25, 12, 22, 11]
selection_sort_with_trace(original2)