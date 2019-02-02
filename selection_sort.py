import random
import numpy as np
import time

###CONSTANTS FOR PROJECT

arr_length = 80000

#start timer for selection sort
start = time.clock()
end=time.time()

##https://www.geeksforgeeks.org/python-program-for-selection-sort/  <---source for selection sort
rev_arr = "test"
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


