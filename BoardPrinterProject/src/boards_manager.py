# place your BoardsManager class in this file
from src import board
class BoardManager(object):
list = ('1. Fill Spot','2. Erase Spot', '3. Switch Board', '4. Create Board','4. Quit' )
    def initialboard(self):
        x = input('Enter string:'\n)
        print(f'Enter the name of your board: {x}')

    def choice(self):
list = ('1. Fill Spot', '2. Erase Spot', '3. Switch Board', '4. Create Board', '4. Quit')
        """#set input value for choices"""
        x = input(int())
        print(f'{x}'\n)
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
while (usr_input != '1') | (usr_input != '2') | (usr_input != '3'):
    if usr_input == '1':
        search()
    elif usr_input == '2':
        search()

        sys.exit()


char square[10] = {'o','1','2','3','4','5','6','7','8','9'};
int checkwin();
void board();
int main()
{
    int player = 1,i,choice;
    char mark;
    do
    {
        board();
        player=(player%2)?1:2;
        cout << "Player " << player << ", enter a number:  ";
        cin >> choice;
        mark=(player == 1) ? 'X' : 'O';

        if (choice == 1 && square[1] == '1')
            square[1] = mark;
        else if (choice == 2 && square[2] == '2')
            square[2] = mark;
        else if (choice == 3 && square[3] == '3')
            square[3] = mark;
        else if (choice == 4 && square[4] == '4')
            square[4] = mark;
        else if (choice == 5 && square[5] == '5')
            square[5] = mark;
        else if (choice == 6 && square[6] == '6')
            square[6] = mark;
        else if (choice == 7 && square[7] == '7')
            square[7] = mark;
        else if (choice == 8 && square[8] == '8')
            square[8] = mark;
        else if (choice == 9 && square[9] == '9')
            square[9] = mark;
        else
        {
            cout<<"Invalid move ";
            player--;
            cin.ignore();
            cin.get();
         }
        i=checkwin();
        player++;
    }while(i==-1);
    board();
    if(i==1)

        cout<<"==>\aPlayer "<<--player<<" win ";
    else
        cout<<"==>\aGame draw";

    cin.ignore();
    cin.get();
    return 0;
}

int checkwin()
{
    if (square[1] == square[2] && square[2] == square[3])
        return 1;
    else if (square[4] == square[5] && square[5] == square[6])
        return 1;
    else if (square[7] == square[8] && square[8] == square[9])
        return 1;
    else if (square[1] == square[4] && square[4] == square[7])
        return 1;
    else if (square[2] == square[5] && square[5] == square[8])
        return 1;
    else if (square[3] == square[6] && square[6] == square[9])
        return 1;
    else if (square[1] == square[5] && square[5] == square[9])
        return 1;
    else if (square[3] == square[5] && square[5] == square[7])
        return 1;
    else if (square[1] != '1' && square[2] != '2' && square[3] != '3'
                    && square[4] != '4' && square[5] != '5' && square[6] != '6'
                  && square[7] != '7' && square[8] != '8' && square[9] != '9')
        return 0;
    else
        return -1;