import random
import numpy as np
import time

arr_length = 1000000

## SOURCE
## https://www.sanfoundry.com/python-program-implement-merge-sort/
def merge_sort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(alist, start, mid)
        merge_sort(alist, mid, end)
        merge_list(alist, start, mid, end)


def merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i = i + 1
        else:
            alist[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            alist[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            alist[k] = right[j]
            j = j + 1
            k = k + 1

##initalize array
alist = np.random.randint(0,9999999,arr_length)
alist = [int (x) for x in alist]
start = time.clock()
merge_sort(alist, 0, arr_length)
end = time.clock()
execution_time = end - start
print(alist, "\n\n")
print("MERGE SORT RANDOM ORDER", execution_time, "SECONDS")
