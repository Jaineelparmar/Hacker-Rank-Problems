# The first line contains the first name, and the second line contains the last name.
# The length of the first and last name ≤10. Print statement "Hello firstname lastname! You just delved into python."

f_n = input("Enter First name: ")
l_n = input("Enter Last name: ")

if (len(f_n) <= 10) and (len(l_n) <= 10):
    print("Hello " + f_n + " " +l_n +"! You just delved into python.")  