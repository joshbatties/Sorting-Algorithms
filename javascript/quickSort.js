function quickSort(arr, left = 0, right = arr.length - 1) {
    // Base case: if the current segment of the array is invalid or has only one element
    if (left >= right) {
        return;
    }

    // Partition the array and get the index of the pivot element after partition
    let pivotIndex = partition(arr, left, right);

    // Recursively apply quicksort to the segments before and after the partition
    quickSort(arr, left, pivotIndex - 1);
    quickSort(arr, pivotIndex + 1, right);

    // Return the sorted array
    return arr;
}

function partition(arr, left, right) {
    // Choose the rightmost element as the pivot
    const pivotValue = arr[right];
    // Starting index of the partition
    let partitionIndex = left;

    // Rearrange the array by comparing each element with the pivot
    for (let i = left; i < right; i++) {
        // If current element is smaller than the pivot, swap it to the correct position
        if (arr[i] < pivotValue) {
            [arr[i], arr[partitionIndex]] = [arr[partitionIndex], arr[i]];
            partitionIndex++;
        }
    }

    // Swap the pivot element to its final position
    [arr[partitionIndex], arr[right]] = [arr[right], arr[partitionIndex]];
    return partitionIndex; // Return the index of the pivot after partitioning
}

// Testing the quickSort function.
console.log(quickSort([121, 12, 132, 51, 61, 99, 200, 0, -1]))