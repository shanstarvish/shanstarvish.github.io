# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.
# Note: Account for all characters that aren't spaces, periods, or commas (Ex: "r", "2", "!").

string = input('Enter Sentence')
count = 0
for ch in string:
    if ch != '.' and ch != ' ' and ch != ',' and ch != '?' and ch != '!':
        count = count + 1

print(count)


