# Given an integer, perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 10, print Weird
# If  is even and greater than 10, print Not Weird

n = int(input('Enter a number:'))

if (n%2 != 0) or ((n%2 == 0) and n in range(6, 21)):
    print('Weird!')

elif ((n%2 == 0) and n in range(2, 6))  or  ((n%2 == 0) and (n > 20)) :
    print('Not Weird!')