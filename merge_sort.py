def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements into 2 halves
        right = arr[mid:]

        # Sorting the first half and second half
        left = merge_sort(left)
        right = merge_sort(right)

        # Merging the sorted halves
        return merge(left, right)
    else:
        # If the array is empty or contains a single element, return it as is
        return arr
    
def merge(left, right):
    result = []  # The merged result
    i, j = 0, 0  # Indexes for left and right arrays

    # Traverse through both arrays and in each iteration add smaller of both elements in 'result'
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Once we reach end of either left or right, pick up the remaining elements and add them
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    print(merge_sort([121, 12, 132, 51, 61, 99]))
