function heapSort(arr) {
    let n = arr.length;

    // Build a maxheap.
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        heapify(arr, n, i);
    }

    // One by one extract elements
    for (let i = n - 1; i > 0; i--) {
        // Swap
        [arr[i], arr[0]] = [arr[0], arr[i]];
        heapify(arr, i, 0);
    }

    return arr;
}

function heapify(arr, n, i) {
    let largest = i; // Initialize largest as root
    let l = 2 * i + 1; // left = 2*i + 1
    let r = 2 * i + 2; // right = 2*i + 2

    // See if left child of root exists and is greater than root
    if (l < n && arr[i] < arr[l]) {
        largest = l;
    }

    // See if right child of root exists and is greater than the largest so far
    if (r < n && arr[largest] < arr[r]) {
        largest = r;
    }

    // Change root, if needed
    if (largest != i) {
        // Swap
        [arr[i], arr[largest]] = [arr[largest], arr[i]];

        // Heapify the root.
        heapify(arr, n, largest);
    }
}
console.log(heapSort([121, 12, 132, 51, 61, 99, 200, 0, -1]));