import re
def fun(s):
    return True if re.match(r'[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[A-Za-z]{0,3}$',s) else False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# NODE                     EXPLANATION
#   ^                        the beginning of the string
#   [a-z]{1}                 any character of: 'a' to 'z' (1 times)
#   [a-z0-9_]{3,13}          any character of: 'a' to 'z', '0' to '9',
#                            '_' (between 3 and 13 times (matching the
#                            most amount possible))
#   $                        before an optional \n, and the end of the
#                            string


# Assert position at the beginning of the string «^»
# Match a single character in the range between “a” and “z” «[a-z]{1}»
#    Exactly 1 times «{1}»
# Match a single character present in the list below «[a-z0-9_]{3,13}»
#    Between 3 and 13 times, as many times as possible, giving back as needed (greedy) «{3,13}»
#    A character in the range between “a” and “z” «a-z»
#    A character in the range between “0” and “9” «0-9»
#    The character “_” «_»
# Assert position at the end of the string (or before the line break at the end of the string, if any) «$»