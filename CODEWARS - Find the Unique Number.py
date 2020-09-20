# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.


# Simple solution, but not as good in performance, codewars will timeout with this code:
def find_uniq(arr):
    for n in arr:
        if arr.count(n) == 1:
            return n


find_uniq([ 1, 1, 1, 2, 1, 1 ])
find_uniq([ 0, 0, 0.55, 0, 0 ])
find_uniq([ 3, 10, 3, 3, 3 ])

# best performance and actually working:


def find_uniq(arr):
    arr.sort() # arrange integers in the array in ascending order

    if(arr[0] < arr[-1] and arr[0] < arr[-2]): # if the first digit in the array is lower than the last and second to last, then n will equal the first digit
        n = arr[0]
    else: # otherwise, n will equal the last digit in the array
        n = arr[-1]


    return n 