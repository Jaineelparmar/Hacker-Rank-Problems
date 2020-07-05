# You are given a string N.
# Your task is to verify that N is a floating point number.

for i in range(int(input())):
    try:
        x=float(input())
        if(x==0):
            print("False")
        else:
            print("True")
    except ValueError:
        print("False")