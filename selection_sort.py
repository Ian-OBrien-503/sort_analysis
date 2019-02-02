import random
import numpy as np
import time

## constant array length setting for RNDM ORDER, PRE-SORTED order, and PRE-REVERSE SORTED ORDER
arr_length = 20000

#start timer for selection sort
start = time.clock()

##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
##start selection sort
arr=np.random.randint(0,99999,arr_length)
##start
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] > arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

print(arr)
end=time.clock()
execution_time = end - start
print("\n\n", execution_time, "seconds of execution for selection sort RNDM ORDER && ARR_SIZE:", arr_length)


################################################################################
################   ASC ORDER PRE-SORTED ORDER     ##############################

##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
##start selection sort BUT DO NOT TIME THIS RUN
arr=np.random.randint(0,99999,arr_length)
##start
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] > arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

start = time.clock()
##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
##start selection sort
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] > arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

print(arr)
end=time.clock()
execution_time = end - start
print("\n\n", execution_time, "seconds of execution for selection sort ASCENDING ORDER && ARR_SIZE:", arr_length)

################################################################################################################
############################ REVERSE ORDER PRE-SORTED ##########################################################


##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
##start selection sort BUT DO NOT TIME THIS RUN
arr=np.random.randint(0,99999,arr_length)
##start
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] < arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

start = time.clock()
##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
##start selection sort
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] > arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

print(arr)
end=time.clock()
execution_time = end - start
print("\n\n", execution_time, "seconds of execution for selection sort REVERSE ORDER && ARR_SIZE:", arr_length)
