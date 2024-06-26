import random

# Text-based Game using dictionaries for organization

# Room dictionary
rooms = {'Coop': {'name': 'Coop',
                  'South': 'The Shed',
                  'West': 'Playhouse',
                  'East': 'Greenhouse',
                  'North': 'Garden',
                  'item': 'No item'
                  },
         'Barn': {'name': 'Barn',
                  'South': 'Greenhouse',
                  'item': 'Scout Wingtip'},
         'Garden': {'name': 'Garden',
                    'East': 'Old Truck',
                    'South': 'Coop',
                    'item': 'Capt. Cluck'},
         'Old Truck': {'name': 'Old Truck',
                       'West': 'Garden',
                       'item': 'Private Peck'},
         'Playhouse': {'name': 'Playhouse',
                       'East': 'Coop',
                       'South': 'Woodpile',
                       'item': 'Col. Plume'},
         'Woodpile': {'name': 'Woodpile',
                      'North': 'Playhouse',
                      'item': 'Villain Reynard the Fox'},
         'The Shed': {'name': 'The Shed',
                      'North': 'Coop',
                      'East': 'Under the Tractor',
                      'item': 'No item'},
         'Greenhouse': {'name': 'Greenhouse',
                        'North': 'Barn',
                        'West': 'Coop',
                        'item': 'Boom-Boom Beak'},
         'Under the Tractor': {'name': 'Under the Tractor',
                               'West': 'The Shed',
                               'item': 'Agent Fluff'}

         }


def instructions():
    # Print main menu and commands
    print('Chicken Army vs Craft Fox')
    print('-------------------------')
    print('A fox has attacked the chicken coop again! You along with General Talon must raise an army!')
    print('Gather all 6 chickens from their hidden locations')
    print('But be careful, the Reynard the Fox is still lurking')
    print('If Reynard finds the General before Talon assembles his Army, that chicken is nuggets!')
    print('-------------------------')
    print('Move Commands: North, South, East or West')
    print('You are starting your search in {}, the last known where abouts of the chickens before they '
          'scattered to the winds.'.format(current_room['name']))
    return


def main(user_input):
    global current_room
    while True:
        print('-----------------------------------------')
        print('Enter Exit at anytime to end the game')
        # Add if statement for winning game here,
        # Check for all the items list
        user_input = input(
            'You must start gathering your army now, what direction would you like to start searching? ').capitalize()
        print('-----------------------------------------')
        if current_room['name'] == 'Exit':
            print('You have decided to give up on this battle. Failing to avenge your fallen comrades,'
                  'and disgracing all chicken kind.')

        # Get user input for moving to each location

        elif user_input in directions:
            if user_input in current_room:
                current_room = rooms[current_room[user_input]]
                print('You are currently in: {}'.format(current_room['name']))
                get_item(current_room)



            else:
                # Move is not possible, bad move
                print('There appears to be no chickens in that direction. Go another way')
        elif user_input == 'Exit':
            print('You have decided to give up on this battle. Failing to avenge your fallen comrades,'
                  'and disgracing all chicken kind.')
            current_room['name'] = 'Exit'
            break
    return user_input


def fight():
    user_input = input('Are you ready for this battle? Say Yes or No\n').capitalize()
    if user_input == 'Yes':
        user_input = input('Type Fight to start!\n').capitalize()
        if user_input == 'Fight':
            i = random.randrange(-1, 2)
            if i >= 0:
                print('The chickens army has prevailed! Reynard the fox is no more!\n', 'YOU HAVE WON!')
            elif i <= 0:
                print('You have lost, despite your bravery and superior numbers. Good luck next time')
        else:
            print('The world has no room for cowards', '\n')
    else:
        print('The world has no room for cowards', '\n')


def get_item(item):
    i = 0
    while i <= 0:
        i = i + 1
        if item == current_room:
            item = current_room['item']
            if item == 'No item':
                print('No chicken here, try again')
                break
        print('You have found a chicken!\n')
        user_input = input('Would you like to take this chicken?: ').capitalize()
        if user_input == 'Yes':
            if current_room['item'] not in chicken_army:
                chicken_army.append(item)
                final_list = set(chicken_army)
                print(final_list, '/n')
                chicken_count = len(final_list)
                if chicken_count >= 6:
                    print('You are ready to take on Reynard the Fox!')
                    fight()
                else:
                    print('Continue recruiting and searching chickens!')


# Beginning of Code
directions = ['North', 'South', 'East', 'West']  # list of available commands / directions
current_room = rooms['Coop']  # Starting location for General Talon / player
chicken_army = []

instructions()
main(current_room)


