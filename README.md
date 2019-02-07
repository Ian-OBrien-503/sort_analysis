#### I used code from the following for...
#### Selection Sort:     https://www.geeksforgeeks.org/python-program-for-selection-sort/ 
#### Merge Sort:         https://www.sanfoundry.com/python-program-implement-merge-sort/

# *selection sort analysis*

expected best:      n^2  
expected worst:     n^2  
expected average:   n^2  

**actual average run-times for #n elements (in seconds)** 

order    | 10,000 | 20,000 | 40,000 | 80,000  
---------|--------|--------|--------|--------  
random   |   16.6 | 66     |  257.3 | 1085  
pre-sort |   16.3 | 63.6   |  253.6 | 1091.6  
reverse  |  17    | 66.6   |  249.3 | 1251  


# *insertion sort analysis*

expected best:      n  
expected worst:     n^2  
expected average:   n^2  

**actual average run-times for #n elements (in seconds)**  

order    | 10,000 | 20,000 | 40,000 | 80,000  
---------|--------|--------|--------|--------  
random   |   21   | 86     |  349.6 | 
pre-sort |  0.004 | 0.009  |  0.013 |   
reverse  |  42.3  | 172.3  |   | 

# *merge sort analysis* 

expected best:      n*log(n)  
expected worst:     n*log(n)  
expected average:   n*log(n)  


**actual average run-times for #n elements (in seconds)** 

order    | 1,000,000 | 2,000,000 | 4,000,000 | 8,000,000  
---------|--------|--------|--------|--------  
random   |   |   |   | 
pre-sort |   |   |   |   
reverse  |   |   |   | 


