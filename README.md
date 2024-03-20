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

# Counting Sort
Counting sort is an integer sorting algorithm. Unlike comparison-based sorting algorithms like quicksort or mergesort, counting sort sorts elements by counting the number of objects that have each distinct key value, and then doing some arithmetic to calculate the position of each object in the output sequence. It works best when the range of input data (the difference between the maximum and minimum element) is not significantly larger than the number of objects to be sorted.

Here's the general approach for implementing counting sort:
1. Find the minimum and maximum values in the input array.
2. Create a count array (or "counting array") that will store the count of each distinct element in the input array. The size of this array should be the range of the input values (max - min + 1).
3. Count each element in the input array and place the count at the appropriate index of the count array.
4. Transform the count array such that each element at each index stores the sum of previous counts. This step makes the count array store the positions of each element in the sorted order.
5. Build the output array by placing input elements at the correct positions in it, decrementing the corresponding counts from the count array.

Time Complexity:
Best, Average, and Worst Cases: O(n + k), where 'n' is the number of elements in the input array, and 'k' is the range of the input (difference between the maximum and minimum elements).
The linear time complexity is because the algorithm processes each of the 'n' elements exactly once and then does additional work that is proportional to 'k' (creating and updating the count array).

Space Complexity:
O(n + k). This is because you need space not only for the counts (which depends on the range of the input values) but also for the sorted output.
It's important to note that while counting sort is efficient in terms of time complexity, especially when 'k' is not significantly larger than 'n', its space complexity can become a limitation if 'k' (the range of input values) is very large.

Stability:
Counting sort is stable, which means that if two elements have the same value, they will retain their relative order in the sorted array as they had in the input array.
This stability is achieved during the final phase of the algorithm, where elements are placed into the output array starting from the end of the input array and decrementing the corresponding counts in the count array. This backward filling ensures that duplicates are placed in the output array in the reverse order they appear in the input, thus maintaining their relative order.

I've adapted the counting_sort function to operate in two modes:
Standard Counting Sort: When called with just the array as an argument, it performs the traditional counting sort, sorting the entire numbers.
Digit-based Counting Sort: When called with a second argument (place), it sorts the array based on the digit in the position indicated by place. This mode is intended for use within radix_sort.

# Radix Sort
Radix sort is a non-comparative sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (i.e., place value). Moving from the least significant digit to the most significant digit, Radix sort uses counting sort as a subroutine to sort. 

Here's the general approach for implementing counting sort:
1. Find the maximum number to know the number of digits.
2. Do the following for each digit i where i varies from the least significant digit to the most significant digit: Sort input array using counting sort (or any stable sort) according to the i-th digit.

Time Complexity:
The total time complexity of Radix Sort is O(kn), where k is the number of digits in the maximum number in the array and n is the number of elements. Since k can be considered O(log10(max_element)), the time complexity is often represented as O(n * log10(max_element)). 

Space Complexity:
?????????

Stability:
The stability of Radix Sort depends on the stability of the sorting algorithm used for sorting individual digits. In this case, because Counting Sort is used, and Counting Sort is stable, Radix Sort remains stable. This is crucial for ensuring that numbers with the same values for earlier digits remain in the same relative order as they were in the original list after all digits have been sorted.

# TODO
quicksort/select

visualisations

