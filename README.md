# Sorting-Algorithms
A collection of all the sorting algorithms introduced in Monash University's FIT2004: Algorithms and Data Structures

# Insertion Sort:
This sorting algorithm is simple to understand and implement, efficient for (small) datasets, more efficient in practice than most other simple quadratic algorithms such as selection sort or bubble sort, and it works well when the data is already partially sorted.

Here's the general approach for implementing insertion sort:

1. Iterate from the second element of the array (index 1) to the last element.
2. Compare the current element with its predecessor.
3. If the current element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped elements.

Time Complexity:
Best Case (Already Sorted List): The best-case scenario occurs when the array is already sorted. In this case, each element is compared only once with the previous element, and since it's already in the correct position, no swaps are needed. Therefore, the best-case time complexity is O(n), where n is the number of elements in the array.

Worst Case (Reversely Sorted List): The worst-case scenario happens when the array is sorted in reverse order. In this case, each new element needs to be compared with each of the already sorted elements and then placed at the beginning of the array. This gives a worst-case time complexity of O(n²).

Average Case: For an average case scenario, where the array is in random order, the average time complexity is also O(n²). 

Space Complexity:
The space complexity of Insertion Sort is O(1). This is because Insertion Sort is an in-place sorting algorithm, meaning it does not require any additional storage apart from the input list. It uses only a constant amount of additional memory space for variables used in the algorithm (like the key and the index variables), which makes it space-efficient.

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
Worst/Best: The time complexity of selection sort is O(n²), where n is the number of elements in the array. This is because for each element of the array, the algorithm scans the remaining elements to find the minimum (or maximum), which leads to a total of about 1/2 * n * (n-1) comparisons, which simplifies to O(n²). The time complexity of selection sort does not actually depend on the arrangement of the elements in the array. 

Space Complexity:
The space complexity of selection sort is O(1), meaning it requires a constant amount of extra memory space. This is because the sorting is done in place, and apart from a few variables for indexing and swapping, no additional storage is required regardless of the array size.

Stability:
tability:
A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Selection sort is not stable by nature because it may swap elements far apart, causing equal elements to change their relative order. However, it can be made stable with some modifications.



