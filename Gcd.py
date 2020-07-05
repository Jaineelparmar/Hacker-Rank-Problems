# Write a function which will take two integers as input, and returns the Greatest Common Divisor (GCD) of those two numbers. (use the Euclid’s algorithm for the same)

#######################################################     Recursion      #################################################
# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
  
def hcf(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcf(b,a%b) 

# prints 12 
print ("The gcd of 60 and 48 is : ",end="") 
print (hcf(60,48)) 



#########################################################      Using Loops    #################################################
# Python code to demonstrate naive 
# method to compute gcd ( Loops ) 

def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 
  
a = 60
b= 48 
# prints 12 
print ("The gcd of 60 and 48 is : ",end="") 
print (computeGCD(60,48)) 



#####################################     Using Euclidean Algorithm      ##########################################
# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algo ) 
   
def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
# prints 12 
print ("The gcd of 60 and 48 is : ",end="") 
print (computeGCD(60,48)) 



#################################  math.gcd( x, y )  ###################################
#Parameters : 
#x :  Non-negative integer whose gcd has to be computed.
#y : Non-negative integer whose gcd has to be computed.
#Return Value : 
#This method will return an absolute/positive integer value after calculating the GCD of given parameters x and y.
#Exceptions : 
#When Both x and y are 0, function returns 0, If any number is a character ,Type error is raised.


# Python code to demonstrate gcd() 
# method to compute gcd 


import math 

print ("The gcd of 60 and 48 is : ",end="") 
print (math.gcd(60,48)) 



#Some common Exceptions in this function are :
#Both numbers are 0, gcd is 0
#If only either number is Not a number, Type Error is raised.
# Python code to demonstrate gcd() 
# method exceptions 


import math  

print ("The gcd of 0 and 0 is : ",end="") 
print (math.gcd(0,0)) 

print ("The gcd of a and 13 is : ",end="") 
print (math.gcd('a',13)) 

