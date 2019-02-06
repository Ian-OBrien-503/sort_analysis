import random
import numpy as np
import time

## intialize array
arr_length = 40
arr = np.random.randint(0,99999,arr_length)

##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
arr=np.random.randint(0,99999,arr_length)
##start
start = time.clock()
for i in range(arr_length):
    min_inx = i
    for j in range (i+1, arr_length):
        if (arr[min_inx] > arr[j]):
            min_inx = j
    arr[i], arr[min_inx] = arr[min_inx], arr[i]

end=time.clock()
print(arr)
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

end=time.clock()
print(arr)
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

end=time.clock()
print(arr)
execution_time = end - start
print("\n\n", execution_time, "seconds of execution for selection sort REVERSE ORDER && ARR_SIZE:", arr_length)
