def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def palindrome(s):
    re = reverse(s)
    if re == s:
        return True
    else:
        return False

s1 = "lsdkjfskf"
s2 = "radar"
print(palindrome(s1))
print(palindrome(s2))

