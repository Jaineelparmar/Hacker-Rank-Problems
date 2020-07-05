def minion_game(string):

    vowels = 'AEIOU'
    count = 0
    count1 = 0

    for i in string.upper():       
        if i not in vowels:
            count += 1
        else:
            count1 += 1
   
    if count == count1:
        print('Draw')
    elif count > count1:
        print('Stuart is Winner')
    elif count < count1:
        print('Kevin is Winner')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)


#OR


def minion_game(string):
    
    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    string = string.upper()

    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)