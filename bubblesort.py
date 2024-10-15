# Python program for implementation of Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Flag to check if a swap was made

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set flag to True if a swap occurs

        # If no two elements were swapped in the inner loop, break
        if not swapped:
            break

# Driver code to test the above function
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("Sorted array is:")
print(arr)  # Print the sorted array directly
