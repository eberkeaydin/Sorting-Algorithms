# Python program for implementation of Insertion Sort
# Let's consider we have an array like : [22, 27, 16, 2, 18, 6].
# If we want to sort this array with using Insertion Sort method:
# Let us loop for i = 1 (second element of the array) to 6 (last element of the array)

# 1) Pass the first element. --> i = 1
# 2) 27 is greater than previous element 22. So, no elements must be moved. --> i = 2
# 3) Next element is 16 and 16 is less than 22. So, move the 16 to top. --> i = 3
# After step 3 we have the current array like [16, 22, 27, ... , 6]
# 4) Next element is 2 and 2 is less than 16. So, move the 2 to top. --> i = 4
# After step 4 we have the current array like [2, 16, 22, 27, ... , 6]
# 5) Next element is 18 and 18 is less than 22. So, move the 18 to second index. --> i = 5
# After step 5 we have the current array like [2, 16, 18, 22, ... , 6]
# 5) Next element is 6 and 6 is less than 16. So, move the 6 to first index. --> i = 6
# After step 5 we have the sorted array like [2, 6, 16, 18, 22, 27]


# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [22, 27, 16, 2, 18, 6]
insertionSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])

# Time complexities for Insertion Sort :
# Best : O(n) | Average : Θ(n^2) | Worst : Θ(n^2) For example number of 18 which is in index of 4 have complexity value : Θ(n^2)
# Another array : [7,3,5,8,2,9,4,15,6] --> [3,7,5,8,2,9,4,15,6] --> [3,5,7,8,2,9,4,15,6] --> [2,3,5,7,8,9,4,15,6] --> so on.
