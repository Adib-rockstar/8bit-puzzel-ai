#8-bit problem
from os import system
import random
def instruction():
    system('cls');
    print("Welcome to my 8-bit program");
    print("Its a simple game, where you will recieve \njumble numbers and you have to arrange them properly as shown below:\n");
    print("_____________");
    print("| 1 | 2 | 3 |");
    print("_____________");
    print("| 4 | 5 | 6 |");
    print("_____________");
    print("| 7 | 8 |   |");
    print("_____________");
    print("\n");
    print("RULES--");
    print("1. You can move 1 number at a time.");
    print("2. You can only swap the number with the blank box.");
    print("3. Only the neighbouring numbers of blank box can be swapped:");
    print("4. The default positon of the box will be shared with you so its easy to swap the numbers, \n    this will be given when you will start the game:");
    print("*******************************************************");
    print("\n");
    print("\n");
    x=input("If you wish to play the game press 1 or exit press any key :- ");
    if(x=='1'):
        randomNumbers();
    else:
        print("--See you soon--");

def randomNumbers():
    system('cls');
    jumbmat=[[0,0,0],[0,0,0],[0,0,0]];
    usermat=[[0,0,0],[0,0,0],[0,0,0]];
    numbers=[0,1,2,3,4,5,6,7,8];
    count=0
    random.shuffle(numbers);
    for i in range(0,3):
        for j in range(0,3):
            if(numbers[count]==0):
                jumbmat[i][j]=' ';
                count=count + 1;
            else:
                jumbmat[i][j]=numbers[count];
                count=count + 1;
    game1(jumbmat);

def game1(jumbmat):
    system('cls');
    count = 1;
    print("\t\t\t\t\t    INDEX OF THE GAME,THIS WILL HELP YOU TO SWAP");
    for i in range(0,3):
        print("_____________",end=""),
        print("\t\t\t\t\t         ",end=""),
        print("_____________");
        for j in range(0,3):
            print("|",jumbmat[i][j],end=" "),
        print("|\t\t\t\t\t\t",end=" ");
        for j in range(0,3):
            print("|",count,end=" ");
            count=count+1;
        print("|",end="");
        print();
    print("_____________",end=""),
    print("\t\t\t\t\t         ",end=""),
    print("_____________");
    game2(jumbmat);

def game2(jumbmat):
    won=check(jumbmat);
    if (won == 1):
        print("You have won the game-");
    print("\n\n\n");
    index=int(input("Enter the index you want to swap with the blank space :- "));
    count = 1;
    for i in range(0,3):
        for j in range(0,3):
            if (jumbmat[i][j] == ' '):
                blank = count;
            else:
                count = count + 1;
    if (blank == index):
        print("You have enter the blank space index number ");
    elif(index == 1 and  (blank == 2 or blank == 4)):
        temp=jumbmat[0][0];
        jumbmat[0][0]=' ';
        if(blank == 2):
            jumbmat[0][1]=temp;
        elif (blank == 4):
            jumbmat[1][0]=temp;
        game1(jumbmat);

    elif(index == 2 and  (blank == 1 or blank == 3 or blank == 5)):
        temp=jumbmat[0][1];
        jumbmat[0][1]=' ';
        if(blank == 1):
            jumbmat[0][0]=temp;
        elif (blank == 3):
            jumbmat[0][2]=temp;
        elif (blank == 5):
            jumbmat[1][1]=temp;
        game1(jumbmat);

    elif(index == 3 and  (blank == 2 or blank == 6)):
        temp=jumbmat[0][2];
        jumbmat[0][2]=' ';
        if(blank == 2):
            jumbmat[0][1]=temp;
        elif (blank == 6):
            jumbmat[1][2]=temp;
        game1(jumbmat);

    elif(index == 4 and  (blank == 1 or blank == 5 or blank == 7)):
        temp=jumbmat[1][0];
        jumbmat[1][0]=' ';
        if(blank == 1):
            jumbmat[0][0]=temp;
        elif (blank == 5):
            jumbmat[1][1]=temp;
        elif (blank == 7):
            jumbmat[2][0]=temp;
        game1(jumbmat);

    elif(index == 5 and  (blank == 2 or blank == 4 or blank == 6 or blank == 8)):
        temp=jumbmat[1][1];
        jumbmat[1][1]=' ';
        if(blank == 2):
            jumbmat[0][1]=temp;
        elif (blank == 4):
            jumbmat[1][0]=temp;
        elif (blank == 6):
            jumbmat[1][2]=temp;
        elif(blank == 8):
            jumbmat[2][1]=temp;
        game1(jumbmat);

    elif(index == 6 and  (blank == 3 or blank == 5 or blank == 9)):
        temp=jumbmat[1][2];
        jumbmat[1][2]=' ';
        if(blank == 3):
            jumbmat[0][2]=temp;
        elif (blank == 5):
            jumbmat[1][1]=temp;
        elif (blank == 9):
            jumbmat[2][2]=temp;
        game1(jumbmat);

    elif(index == 7 and  (blank == 4 or blank == 8)):
        temp=jumbmat[2][0];
        jumbmat[2][0]=' ';
        if(blank == 4):
            jumbmat[1][0]=temp;
        elif (blank == 8):
            jumbmat[2][1]=temp;
        game1(jumbmat);

    elif(index == 8 and  (blank == 7 or blank == 5 or blank == 9)):
        temp=jumbmat[2][1];
        jumbmat[2][1]=' ';
        if(blank == 7):
            jumbmat[2][0]=temp;
        elif (blank == 5):
            jumbmat[1][1]=temp;
        elif (blank == 9):
            jumbmat[2][2]=temp;
        game1(jumbmat);

    elif(index == 9 and  (blank == 6 or blank == 8)):
        temp=jumbmat[2][2];
        jumbmat[2][2]=' ';
        if(blank == 6):
            jumbmat[1][2]=temp;
        elif (blank == 8):
            jumbmat[2][1]=temp;
        game1(jumbmat);

def check(jumbmat):
    checkmat=[[1,2,3],[4,5,6],[7,8,9]];
    checkmat[2][2]=' ';
    for i in range(0,3):
        for j in range(0,3):
            if(checkmat[i][j] == jumbmat[i][j]):
                won = 1;
            else:
                return 0;
    return 1;



instruction()
