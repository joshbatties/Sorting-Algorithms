def insertion_sort(arr):
    # Loop from the second element (index = 1) of the array until the last, 
    # position the element in its correct place relative to the sorted part of the array
    for i in range(1, len(arr)):
        # This is the element we are positioning in its correct place, relative to sorted part
        current = arr[i]

        # Initialize j to be the previous element's index, for comparison
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than current,
        # to one position ahead of their current position if they are greater than current
        while j >= 0 and current < arr[j]:
            # Move to the previous element
            arr[j + 1] = arr[j]
            j -= 1  

        # Place current after the element just smaller than it.
        arr[j + 1] = current

    # Return the sorted array
    return arr


if __name__ == "__main__":
    print(insertion_sort([121, 12, 132, 51, 61, 99, 200, 0, -1]))
