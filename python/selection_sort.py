def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element, if needed
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # Return the sorted array
    return arr


if __name__ == "__main__":
    print(selection_sort([-1, 121, 12, 132, 51, 61, 99, 0, -4]))
