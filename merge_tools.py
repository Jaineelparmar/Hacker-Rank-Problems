def merge_the_tools(string, k):

    set1 = set()   
    for i in range(0, len(string), k):
        no_dup_str = ''

        for ch in string[i : i+k]:
            if ch not in set1:
                set1.add(ch)
                no_dup_str += ch
        print(no_dup_str)

        set1 = set()   

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)