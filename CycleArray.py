def rotate(arr, n):
    last_el = arr[n - 1] # Last element of any given array
  
    # Initialize for loop, start at last element, go to first element, go back (steps).
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1] # Shifts the array to the left, remember from right to left, places current index's left element to it's current position.

    arr[0] = last_el # Swap first and last array.


arr = [1, 2, 3, 4, 5]
n = len(arr) # Our whole array length
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ')
