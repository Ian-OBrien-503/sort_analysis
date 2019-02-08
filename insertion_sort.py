import random
import numpy as np
import time

##initalize array to sort
arr_length = 80000
arr = np.random.randint(0,9999999,arr_length)


##start insertion sort RANDOM ORDER based off wikipedia algorithm for insertion
start = time.clock()
i = 1
while i < arr_length:
    j = i
    while j>0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j - 1
    i = i + 1   
end = time.clock()
execution_time = end - start

print(arr)
print("\n\n", execution_time, "seconds of execution time for INSERTION SORT && RANDOM ORDER and ARR_SZ:", arr_length, "\n\n")

##start insertion sort PRE_SORTED ASC
start = time.clock()
i = 1
while i < arr_length:
    j = i
    while j>0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j - 1
    i = i + 1
end = time.clock()
execution_time = end - start

print(arr)
print("\n\n", execution_time, "seconds of execution time for INSERTION SORT && PRE_SORTED ASC and ARR_SZ:", arr_length, "\n\n")

## SORT ARRAY IN DESC ORDER FIRST AND THEN RUN ASC ORDER INSERTION SORT

##reverse the order
i = 1
while i < arr_length:
    j = i
    while j>0 and arr[j-1] < arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j - 1
    i = i + 1

##NOW START TIMER AND SORT ASC
start = time.clock()
i = 1
while i < arr_length:
    j = i
    while j>0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j - 1
    i = i + 1
end = time.clock()
execution_time = end - start

print(arr)
print("\n\n", execution_time, "seconds of execution time for INSERTION SORT && PRE_SORTED REVERSE and ARR_SZ:", arr_length, "\n\n")
