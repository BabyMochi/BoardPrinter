# place your BoardsManager class in this file
from src import board
class BoardManager(object):
    def __init__(self):
    nameboard = input('Enter the name of your board: ')
    numberrows = input('Enter the number of rows for your board: ')
    numbercolumns = input('Enter the number of columns for your board: ')
    charactertype = input ('Enter the blank character to be used on your board: ')
    def initialboard(self):
        x = input('Enter string:'\n)
        print(f'Enter the name of your board: {x}')
    def choice(self):
        print('Select your action from the list below.\n'
              '1. Fill Spot\n'
              '2. Erase Spot\n'
              '3. Switch Board\n'
              '4. Create Board\n'
              '5. Quit\n')
        action_number = input('Enter the number of the action you would like to do: ')
        try:
            action_number = int(action_number)
        except ValueError:
            print(f'You must enter a number between 1 - 5. {action_number} is not a number between 1 - 5.')

        if action_number == 1:
            return self.fill_spot()
        elif action_number == 2:
            return self.erase_spot()

    def fillspot(self):
        x = input(int())
        print(f'{x}''\n)

    def erasespot(self):
        x = input(int())

    def switchboard(self):
        x = input(int())


    def createboard(self):
        x = input(int())


    def quit(self):
        x = input(int())


    def saveboardnames(self):
        x = input(int())


"""#Possible function with while loop"""
usr_input = input("Input: ")
while (usr_input == '1') | (usr_input != '5'):
    if usr_input == '1':
        search()
    elif usr_input == '2':
        search()
    elif usr_input == '3':
        search()
    elif usr_input == '4':
        search()
    else usr_input == '5':
        search()
        sys.exit()


