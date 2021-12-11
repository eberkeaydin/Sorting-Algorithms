# Merge Sort : Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves,
# and then merges the two sorted halves. The merge() function is used for merging two halves.
# The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

# For given array arr = [16,21,11,8,12,22], firstly program finds the mid and divide this array to new two arrays like :
# [16,21,11,8,12,22] --> [16,21,11] and [8,12,22] --> ([16,21,11] --> [16,21] and [11] then --> [11,16,21])
# and ([8,12,22] is sorted already)  -->  [11,16,21] and [8,12,22] to --> [8,11,12,16,21,22]


# Big(O) | Time complexity for given array Best case: Ω(n log(n)) | Average Case :	Θ(n log(n)) | Worst Case: O(n log(n))



# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [16,21,11,8,12,22]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

