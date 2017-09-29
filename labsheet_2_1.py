

def is_palindrome(s):
    s = str(s).lower()

    return s[::-1] == s


def is_palindrome_2(s):
    j = 0
    for i in reversed(s):
        if str(s[j]).lower() != str(i).lower():
            return False
        j += 1

    return True
