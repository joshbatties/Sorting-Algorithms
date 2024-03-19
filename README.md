## Sorting-Algorithms
A collection of all the sorting algorithms introduced in Monash University's FIT2004: Algorithms and Data Structures

# Insertion Sort:
This sorting algorithm is simple to understand and implement, efficient for (small) datasets, more efficient in practice than most other simple quadratic algorithms such as selection sort or bubble sort, and it works well when the data is already partially sorted.

Here's the general approach for implementing insertion sort:

1. Iterate from the second element of the array (index 1) to the last element.
2. Compare the current element with its predecessor.
3. If the current element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped elements.

Time Complexity:
Best Case (Already Sorted List): The best-case scenario occurs when the array is already sorted. In this case, each element is compared only once with the previous element, and since it's already in the correct position, no swaps are needed. 
Therefore, the best-case time complexity is O(n), where n is the number of elements in the array.

Worst Case (Reversely Sorted List): The worst-case scenario happens when the array is sorted in reverse order. In this case, each new element needs to be compared with each of the already sorted elements and then placed at the beginning of the array. 
This gives a worst-case time complexity of O(n²).

Average Case: For an average case scenario, where the array is in random order, the average time complexity is also O(n²). 

Space Complexity:
The space complexity of Insertion Sort is O(1). 
This is because Insertion Sort is an in-place sorting algorithm, meaning it does not require any additional storage apart from the input list. It uses only a constant amount of additional memory space for variables used in the algorithm (like the key and the index variables), which makes it space-efficient.

Stability:
Insertion Sort is a stable sorting algorithm. Stability in a sorting algorithm means that two objects with equal keys appear in the same order in the sorted output as they appear in the input. Insertion Sort maintains this order because when equal elements are encountered, the algorithm does not swap them. Instead, it only moves the new element past them, thereby preserving their original order relative to each other.

# Selection Sort
Selection sort is a simple sorting algorithm that divides the input list into two parts: a sorted subset at the front of the list and an unsorted subset at the rest of the list. Initially, the sorted subset is empty and the unsorted subset is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted subset, swapping it with the leftmost unsorted element (putting it in sorted order), and moving the subset boundaries one element to the right.

Here's the general approach for implementing selection sort:

1. Start with the first element of the array.
2. Search for the smallest element in the array.
3. Swap the smallest element found with the first element.
4. Move to the next element and repeat the process until the entire array is sorted.

Time Complexity:
Worst/Best: The time complexity of selection sort is O(n²), where n is the number of elements in the array. 
This is because for each element of the array, the algorithm scans the remaining elements to find the minimum (or maximum), which leads to a total of about 1/2 * n * (n-1) comparisons, which simplifies to O(n²). The time complexity of selection sort does not actually depend on the arrangement of the elements in the array. 

Space Complexity:
The space complexity of selection sort is O(1), meaning it requires a constant amount of extra memory space. This is because the sorting is done in place, and apart from a few variables for indexing and swapping, no additional storage is required regardless of the array size.

Stability:
A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Selection sort is not stable by nature because it may swap elements far apart, causing equal elements to change their relative order. However, it can be made stable with some modifications.

# Merge Sort
Merge Sort is a divide-and-conquer algorithm that divides the unsorted list into n sublists, each containing one element (a list of one element is considered sorted), and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

Here's the general approach for implementing merge sort:
1. Divide (Splitting the array): If the array contains more than one element, we split it into two halves.
2. Conquer (Sorting each half): We recursively sort both halves of the array.
3. Combine (Merging sorted halves): We merge the two halves to produce a single sorted array.

Time Complexity:
Worst/Best: O(n log n), where 'n' is the number of elements in the array.
This is because the list is being split in half each time (which contributes to the log n part), and then each level of splits needs to be merged back together (which contributes to the n part).

Space Complexity:
The space complexity of Merge Sort is O(n), where 'n' is the number of elements in the array.
This additional space is required for storing the temporary arrays used to merge sorted sections. Even though the merge steps are applied sequentially and in-place merging is possible, the standard implementation of Merge Sort, as presented here, requires additional space proportional to the size of the input array for the duration of the sorting process.

Stability:
Merge Sort is a stable sorting algorithm. 
This means that if two elements have equal values, they will retain their relative order in the sorted array. The stability is ensured during the merging process: when two elements from different halves are equal, the element from the left half (which originally came first) is always chosen first, preserving order among equal elements.

# Heap Sort
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It's similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

Here's the general approach for implementing heap sort:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree.
3. Repeat step 2 while the size of the heap is greater than 1.

Time Complexity:
Best Case: The best-case time complexity of Heap Sort is O(n log n), which occurs when the input array is already a heap.

Average Case: The average-case time complexity of Heap Sort is also O(n log n). 
Regardless of the initial order of the elements, the total time to build the heap is O(n), and the time to delete all elements from the heap (heapify each time) is O(n log n).

Worst Case: The worst-case time complexity is also O(n log n). 
Even in the worst case, heap sort makes a log n number of comparisons for each of the n elements.

Space Complexity:
Heap Sort has a space complexity of O(1) beyond the original array. This is because Heap Sort is an in-place sorting algorithm; it does not require any extra space beyond what is needed to hold the original array.

Stability:
Heap Sort is not a stable sorting algorithm. Stability in sorting algorithms is the property that ensures that two records with equal keys appear in the same order in sorted output as they appear in the input unsorted array. Since Heap Sort operates based on a binary heap structure and may move elements around in the heap during the sorting process, it can change the relative order of equal elements, hence it is not stable.

# TODO
counting sort
radix sort
quicksort/select

visualisations

