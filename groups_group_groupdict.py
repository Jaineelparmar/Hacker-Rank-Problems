# import re
# m = re.search(r'([a-zA-Z0-9])\1+',input().strip())
# if m:
#     print(m.group(1))
# else:
#     print(-1)

# import re
# m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
# print(m.group(1) if m else -1)

s = list(input())
for i in range(len(s)): 
    try:
        if s[i] == s[i+1]:
            if s[i].isalnum():
                print(s[i])
                break
    except:
        print("-1")