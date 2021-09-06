from random import randint
condition = True


while condition:
    try:
        amount_players = int(input('1. Play vs AI. \n'
                               '2. Simulate rock, paper & sissorcs \n'
                               '3. Quit \n'))
        if amount_players == 3:
            condition = False
        elif amount_players == 1:
            pass
        elif amount_players == 2:
            pass
    except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))


