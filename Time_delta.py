#!/bin/python3
from datetime import datetime
import os

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    fmt = '%a %d %b %Y %H:%M:%S %z'   #day dd mon yyyy hh mm ss utc
    t1 = datetime.strptime(t1, fmt)
    t2 = datetime.strptime(t2, fmt)
    result = (int( abs((t1 - t2).total_seconds()) ))
    return str(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()