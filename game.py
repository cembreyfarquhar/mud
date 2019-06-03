from player import Player

print('Welcome! Start by creating a pllayer')


def create_player():
    while True:
        cmd = input('Press "r" to roll for your stats. Press "c" to continue. ')
        if cmd == 'r':
            user = Player()
        if cmd == 'c':
            return user


user = None

while True:
    cmd = input('')
    # Create the user!
    if user == None:
        user = create_player()
    print('enter a command')
    if cmd == 'user':
        print(user.stats)
