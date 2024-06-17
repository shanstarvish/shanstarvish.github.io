input_month = input('Enter')
input_day = input('Enter number')

monthTuple = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December'}

input_day = input_day.strip()
input_day = int(input_day)

input_month = input_month.strip().capitalize()


# validate month input


# validate input
if not (input_month in monthTuple):
    print('Invalid')


# Checking for Spring: March 20-31, April and May 1-30, June 1-20

elif input_month == 'March':
    if not (1 <= input_day <= 31):
        print('Invalid')
    elif input_day <= 19:
        print('winter')
    else:
        print('Spring')
elif input_month == 'April':
    if not (1 <= input_day <= 30):
        print("Invalid")
    else:
        print("Spring")
elif input_month == 'May':
    if not (1 <= input_day <= 31):
        print("Invalid")
    else:
        print("Spring")
elif input_month == 'June':
    if not (1 <= input_day <= 30):
        print("Invalid")
    elif input_day <= 20:
        print("Spring")
    else:
        print("Summer")
elif input_month == 'July' or input_month == 'August':
    if not (1 <= input_day <= 31):
        print("Invalid")
    else:
        print("Summer")
elif input_month == 'September':
    if not (1 <= input_day <= 30):
        print("Invalid")
    elif input_day <= 21:
        print("Summer")
    else:
        print("Autumn")
elif input_month == "October":
    if not (1 <= input_day <= 31):
        print("Invalid")
    else:
        print("Autumn")
elif input_month == "November":
    if not (1 <= input_day <= 30):
        print("Invalid")
    else:
        print("Autumn")
elif input_month == "December":
    if not (1 <= input_day <= 31):
        print("Invalid")
    elif input_day <= 20:
        print("Autumn")
    else:
        print("Winter")
elif input_month == 'January':
    if not (1 <= input_day <= 31):
        print("Invalid")
    else:
        print("Winter")
elif input_month == "February":
    if not (1 <= input_day <= 29):
        print("Invalid")
    else:
        print("Winter")





