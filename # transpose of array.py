import numpy as np 
  
arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 

print ("Cumulative sum along each row:\n", arr.cumsum(axis = 0)) 