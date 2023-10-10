def reverse(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


A = [1, 2, 3, 4, 5, 6]
end_arr = len(A) - 1
print(f"given array is:\n{A}")

reverse(A, 0, end_arr)
print(f"Reversed array:\n{A}")
