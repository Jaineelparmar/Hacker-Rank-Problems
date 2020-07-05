n = int(input('Enter upto ?'))

if(n >= 1 and n <= 20):
    i = 0
    while(i <= n):
        res = i*i
        print('Square of '+ str(i) +' is: '+ str(res))
        i=i+1