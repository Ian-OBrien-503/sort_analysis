#### I used code from the following for...
#### Selection Sort:     https://www.geeksforgeeks.org/python-program-for-selection-sort/ 
#### Merge Sort:         https://www.sanfoundry.com/python-program-implement-merge-sort/

# *preface*  

I choose to implement my project in python, something I have never done before and thought that I would run into a lot more issues than I really would.  The fact that python is loosely typed and has great libraries for arrays and timing things, it made developing the tests quite easy.  Making large random arrays with various sizes and order was much easier than doing
it in C.  

I also choose to report my results via git-hub and including all my files on the web which I had a general idea how to do,  
and the only semi-difficult part was learning some basic markdown to format this report.  

I am timing the algorithms with the time library for python and using time.clock() and some basic arithmetic to get good approximations.  I used my home laptop with Linux mint, writing the code using python 3.5 in a PyCharm editor.  The only real issue that I encountered was the fact that python stores integers as 16-byte objects.  I am limited to 8GB of ram, and when running tests for the merge sort we sorted lists of up to 16 million integers.  If I had choose to get very very large input sizes outside of the size of my ram that may have affected runtime to reach out to the disk to get some of the data. 



# *selection sort analysis*

expected best:      O(n^2)  
expected worst:     O(n^2)  
expected average:   O(n^2)

*experiemental time-complexity in all cases run: 0(n^2)*

**actual average run-times for #n elements (in seconds)** 

order    | 10,000 | 20,000 | 40,000 | 80,000  
---------|--------|--------|--------|--------  
random   |   16.6 | 66     |  257.3 | 1085  
pre-sort |   16.3 | 63.6   |  253.6 | 1091.6  
reverse  |  17    | 66.6   |  249.3 | 1251  

The expected run time in all cases for selection sort is n^2, that is the average, worst, and best cases all have the same
time complexity class O(n^2). This is the nature of the selection sort algorithm, that is, it iterates through the array
each time to find the next smallest number (assuming sorting in ASC order).

The data collected on the selection sort seems to show that the complexity of the applied algorithm holds true to the class of O(n^2). We can see that for each double in size of the input there is an approximately four-fold increase in the run time.
This is not exact, but I would claim that the constant for this case would be somewhere just slightly above 1, which can be ignored anyways in classifying the complexity. Additionally, it seems under all of the cases that the run time was consistent.  Which is what we expected for selection sort.  

# *insertion sort analysis*

expected best:      O(n)  
expected worst:     O(n^2)  
expected average:   O(n^2)  

*experimental time-complexity for pre-sorted order:  O(n)*  
*experimental time-complexity for random order:  O(n^2)*  
*experimental time-complexity for reverse order:  O(n^2)*  

**actual average run-times for #n elements (in seconds)**  

order    | 10,000 | 20,000 | 40,000 | 80,000  
---------|--------|--------|--------|--------  
random   |   21   | 86     |  349.6 |  1376
pre-sort |  0.004 | 0.009  |  0.013 |  0.038
reverse  |  42.3  | 172.3  | 700.6  |  2768

**NOTE:  
only performed one run for each case for input size of 80,000 since runs took so long. Time seemed consistent  with the 
rest of the data, if had more time would perform more tests**

Our results are slightly more interesting for the insertion sort. In the case of a pre-sorted array, we have a very small run-time, that is hard to compare from input size to input size, at least from what was selected. However, we can see that for each double in the size of the input for the insertion sort, we also see an approximate double in the run time. This
would suggest that the best case is the pre-sorted case for insertion sort. That is because in the case that the array
is pre-sorted that the algorithm doesn't really have to do any work except traverse the array and do the comparisons to
verify that it is already in order. We expect linear run-time in this case, and we get linear run time in this case.

The other cases where the list is in either random order or reverse order (pre-sorted in DESC order) we see some interesting
results as well. We see that in each case each time the input doubles in size that the time to run increases approximately
four-fold, respective to their pre-sort condition. This implies that in the average case, which would be random order that
we get 0(n^2) time-complexity, and in the worst case we get 0(n^2) time-complexity as well.

It is worth noting that when the list is in reverse order it takes approximately twice as long to sort as the random
order. That's because the reverse order sort is making the algorithm do that maximum amount of "work", comparison's and
swaps that it can. It stays in 0(n^2) complexity class though because in this case relative to the input sizes, when the
input size doubles the run-time increases approximately four-fold. Even if it is twice as long run-time as a pre-sorted list
it still remains in the 0(n^2) complexity class.

# *merge sort analysis* 

expected best:      0(n\*log(n))  
expected worst:     0(n\*log(n))  
expected average:   0(n\*log(n))  

*experimental time-complexity for all cases run:  ~0(n\*log(n))*  

**actual average run-times for #n elements (in seconds)** 

order    | 1,000,000 | 2,000,000 | 4,000,000 | 8,000,000  
---------|-----------|-----------|-----------|--------  
random   |  17.0     |   35.4    |    79.2   | 155
pre-sort |  13.2     |  28.7     |    62.1   |   132.6
reverse  |  15.2     |   30.2    |  62.6     |  134

The final sort that was analyzed was the merge sort.  It seems to be the best sort for the cases that we tested for in terms of run-time.  It is important to consider why the expected runtime is n*log(n).  We have a log(n) run-time because we are splitting the problem size in half at each step of the algorithm, and at each step in the merge, we have to compare n,  
n elements.  There will be a constant multiplier in these cases that will vary depending on the number of steps you had to take to merge all of the data back together.  As stated previously this constant is ignored and we can claim 0(n\*logn) time complexity.  

It is worth noting also that n*logn runtime is worse than long runtime and worse than linear runtime.  Basically, it is
linear run time multiplied by the log of the constant, which turns out to be relatively small compared to say n^2 time.
For very large inputs this is nearly linear but slightly worse, which holds true ion our analysis of the run-times. 
Also regardless of the condition of the array before merge-sort begins it performs approximately the same under all conditions, which is the expected behavior of the merge sort algorithm. 


# *conclusions...*

It seems that the selection sort and insertion sort were not the most useful sorts.  They would perform fine for small tasks needed to sort the list of size 100 or less which may be useful for some small applications interpreting small sets of data. The ease of implementation of these algorithms makes these much more desirable to choose for cases like these.
I suppose insertion sort could be useful to check a large set of data to tell you whether it was in order or not, but not very useful for actually performing the sort. 

Merge sort seems much more useful for larger scale applications like sorting customer data from a database, or complex scientific applications where order matters on large sets of data.  The good news for the merge sort also is regardless
of the condition of the data pre-sort you have a relatively fast sort time, even for large data sets.  I was very impressed
that I could sort 16 million integers in any order in approximately 130 seconds.  The tradeoff here is that the implementation of the merge sort is significantly more difficult.  

All in all, each algorithm has its trade-offs in terms of ease of implementation vs performance, but we should really avoid
using sorts similar to selection or insertion sort for large sets of data at all costs. 

