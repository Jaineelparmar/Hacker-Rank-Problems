Learn more or give us feedback
# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=int(input(""))
b=int(input(""))
print('{0}\n{1}\n{2}'.format((a + b), (a - b), (a * b)))




#Read two integers and print two lines.
# The first line should contain integer division. The second line should contain float division.

i=int(input("Enter a number"))
j=int(input("Enter a number"))
print('{0}\n{1}'.format(i//j, i/j))
