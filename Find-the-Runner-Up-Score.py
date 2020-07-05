#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':

    arr = map(int, input().split())
    y = []

    for i in arr:
        y.append(i)
    #print(y)

    y.sort(reverse = True)
    #print(y)

    for i in range(len(y)-1):
        #print(i) 

        if y[i] != y[i+1]:
            print(y[i+1])
            break


