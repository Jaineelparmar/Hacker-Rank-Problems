# import re
# for i in range(int(input())):
#     try:
#         print(bool(re.compile(input())))
#     except re.error:
#         print(False) 


# import re
# for i in range(int(input())):
#     try:
#         print(bool(re.compile(input())))
#     except Exception:
#         print(False) 


import re
for i in range(int(input())):
    try:
        a = re.compile(input())
        print(True)
    except re.error:
        print(False) 