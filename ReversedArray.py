# Function to reverse an array in-place
def reverse(A, start, end):
    while start < end:
        # Swap the elements at the 'start' and 'end' positions
        A[start], A[end] = A[end], A[start]
        # Increment 'start' (moving from 0 towards the center)
        start += 1
        # Decrement 'end' (moving from the end towards the center)
        end -= 1

# Example usage
A = [1, 2, 3, 4, 5, 6]
end_arr = len(A) - 1  # Get the index of the last element
print(f"Given array is:\n{A}")

# Call the 'reverse' function to reverse the array
reverse(A, 0, end_arr)  # Using variables for clarity
print(f"Reversed array:\n{A}")
