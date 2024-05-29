# Many user-created passwords are simple and easy to guess. Write a program that
# takes a simple password and makes it stronger by replacing characters using
# the key below, and by appending "q*s" to the end of the input string.

# i becomes !
# a becomes @
# m becomes M
# B becomes 8
# o becomes .

word = input('Choose password')
password = ''

for ch in word:
    password = password + ch
    password = password.replace('a', '@')
    password = password.replace('i', '!')
    password = password.replace('m','M')
    password = password.replace('B','8')
    password = password.replace('o','.')

print(password + 'q*s')
