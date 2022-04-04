from queue import PriorityQueue
from traceback import print_tb
from types import SimpleNamespace
from Board import *
from Others import *
import time
import msvcrt

def inputPilihan():
    looping = True
    time.sleep(0.8)
    print("(1) for file input        (3) for random input")
    print("(2) for manual input      (99) exit the program")
    print()
    op = int(input("Choose a number (1) or (2) or (3) or (99) : "))
    print()
    while not(op==1 or op==2 or op==3 or op==99):
        print("YOUR INPUT NOT VALID..!! Please reinput a number within range..!!")
        op = int(input("Choose a number (1) or (2) or (3) or (99) : "))
        print()
    if op == 1:
        file = input("Now, please input your filename (without extension) : ")
        Mtr = readFile(file)
    elif op == 2:
        Mtr = readManual()
    elif op == 3:
        Mtr = simpleRandomize()
    elif op ==99:
        print("Thanks a lot for using our porgram...!!  />..<\\")
        print("Have a nice day..!!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        Mtr = []
        
    return Mtr

print("""
                                    <------>     ____ _______
     _______                        __          /_   |   ____|
    |   __  \  --->  ->  --->      |  |  ___   /__   |  |
    |  |  |  |     <---  <-  <---  |  |/ __ \ /__ |  |  |____
    |  |_/ _/__    __ _____________|  | |__|/     |++|_____  \\
    |   __/ |  |  |  |__   /|__   /|  |  __/__    |++|    |  | 
    |  |    |  |  |  | /  /   /  / |  |\______|   |  |    /  |
    |  |    |   ++   |/  /_  /  /_ |  |___________|__|___/   /
    |__|     \______//_____|/_____||_________________|______/
""")
time.sleep(1)
print("WELCOME to Puzzle-15 BOARD GAME...!!!")
print()
time.sleep(1.2)
print("This game will be solved by our automatic system,..")
time.sleep(1)
print("You only need to input the Initiate BOARD configuration,..")
time.sleep(1)
print("There are 3 ways to do it,.. let's check it out..!")
time.sleep(1)
print()
print("Press anykey to continue..!" )
trash = msvcrt.getch()
time.sleep(0.3)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(0.6)
print("--> 1st Way : BOARD Configuration inputed by text file (.txt)")
print("              You can input the file name that stored at folder \"test\"")
print("              example : \"in1\" for in1.txt text file")
print()
time.sleep(1)
print("--> 2nd Way : BOARD Configuration manually inputed")
print("              You can input the matrix with 4x4 size that separated by space")
time.sleep(0.5)
print("""              example : 1  2  3  4
                        5  6  7  8
                        9 10 11 12
                       13 14 15 16 """)
print()
time.sleep(1)
print("--> 3rd Way : BOARD Configuration generated randomly by our system")
print("              Note : BOARD will be showed later")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    Mtr = inputPilihan()
    if Mtr==[]:
        break
    
    board = Board(Mtr)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--> HERE IS YOUR INITIAL STATE of PUZZLE-15 <--")
    board.printMatrix()
    print()
    time.sleep(0.8)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("--> HERE IS THE CHECKING TABLE of BOUND <--")
    board.printKURANGI()
    print()
    time.sleep(0.8)

    bound, can = board.BOUNDING()
    print(f"Nilai dari sum_KURANG(i) + X adalah {bound}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if not(can):
        print("--->>    !...WARNING...!    <<---")
        print("This Puzzle-15 can not be solved..! Because, its BOUNDING VALUE is ODD...")
    else:
        # DEKLARASI
        # PQ = []                                               # LIST IMPLEMENT
        PQ = PriorityQueue()                                    # Prio IMPLEMENT
        node_created = SimpleNamespace()
        node_created.count = 0
        
        # INISIALIASI Puzzle awal di dalam antrian
        # PQ.append( (0,board) )                                # LIST IMPLEMENT                        
        PQ.put( (0,board) )                                     # Prio IMPLEMENT
        node_created.count += 1
        
        start = time.time()
        # while not( isGOAL_STATE(PQ[0][1].getMatrix()) ):      # LIST IMPLEMENT
        while not( isGOAL_STATE(PQ.queue[0][1].getMatrix()) ):  # Prio IMPLEMENT
            
            # Expand simpul pertama yang ada pada antrian
            # currBoard = PQ[0][1]                              # LIST IMPLEMENT
            # PQ.pop(0)                                         # LIST IMPLEMENT
            currBoard = PQ.get()[1]                             # Prio IMPLEMENT
            
            xn, yn = currBoard.getBlank()
            
            # 1. Raising child node based on move Up
            if (xn != 0) and (currBoard.getprev_path()[-1] != "d"):
                new1 = deepcopy(currBoard)
                new1.move("u")
                moveProgress(new1,currBoard.getprev_path(),"u",PQ,node_created)
            
            # 2. Raising child node based on move Right
            if (yn != 3) and (currBoard.getprev_path()[-1] != "l"):
                new2 = deepcopy(currBoard)
                new2.move("r")
                moveProgress(new2,currBoard.getprev_path(),"r",PQ,node_created)
            
            # 3. Raising child node based on move Down
            if (xn != 3) and (currBoard.getprev_path()[-1] != "u"):
                new3 = deepcopy(currBoard)
                new3.move("d")
                moveProgress(new3,currBoard.getprev_path(),"d",PQ,node_created)
            
            # 4. Raising child node based on move Down
            if (yn != 0) and (currBoard.getprev_path()[-1] != "r"):
                new4 = deepcopy(currBoard)
                new4.move("l")
                moveProgress(new4,currBoard.getprev_path(),"l",PQ,node_created)
                
        stop = time.time()
        timeTaken = (stop-start)
        
        print("-->     !...SOLUTION FOUND...!     <--")
        print()
        time.sleep(1)
        print("--> INITIAL STATE of PUZZLE-15 <--")
        board.printMatrix()
        print()
        
        i = -1
        # for direction in PQ[0][1].getprev_path():             # LIST IMPLEMENT
        for direction in PQ.queue[0][1].getprev_path():         # Prio IMPLEMENT
            if i == -1:
                i += 1
                continue
            i += 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("--> Taken MOVE : ",end="")
            if direction == "u":
                print("ATAS")
                board.move("u")
            elif direction == "r":
                print("KANAN")
                board.move("r")
            elif direction == "d":
                print("BAWAH")
                board.move("d")
            elif direction == "l":
                print("KIRI")
                board.move("l")
            print()
            board.printMatrix()
            print()
            time.sleep(1)

        print(f"Program Execution time : {timeTaken} seconds")
        print(f"                       : {timeTaken*1000} miliseconds")
        print(f"Count of Move Taken : {i}")
        print("Path that able to take : ",end="")
        PQ.queue[0][1].printPATH()
        print(f"Count of Raised Node (living-node ever) : {node_created.count}")
        
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

