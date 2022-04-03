from types import SimpleNamespace
from Board import *
from Others import *
import time

board = Board(readFile("in.txt"))
board.printKURANGI()
print()

bound, can = board.BOUNDING()
print(f"Total KURANG(i) + X adalah {bound}")

if not(can):
    print("Puzzle-15 ini Tidak Dapat Diselesaikan..!")
else:
    # DEKLARASI
    PQ = []
    node_created = SimpleNamespace()
    node_created.count = 0
    
    # INISIALIASI Puzzle awal di dalam antrian
    PQ.append( (0,board) )
    node_created.count += 1
    
    start = time.time()
    while not( isGOAL_STATE(PQ[0][1].getMatrix()) ):
        # Urutkan berdasarkan prioritas
        # PQ.sort(reverse=True)
        
        # Expand simpul pertama yang ada pada antrian
        currBoard = PQ[0][1]
        PQ.pop(0)
        
        # 1. Raising child node based on move Up
        x1, _ = currBoard.getBlank()
        if (x1 != 0) and (currBoard.getprev_path()[-1] != "d"):
            new1 = deepcopy(currBoard)
            new1.move("u")
            moveProgress(new1,currBoard.getprev_path(),"u",PQ,node_created)
        
        # 2. Raising child node based on move Right
        _, y2 = currBoard.getBlank()
        if (y2 != 3) and (currBoard.getprev_path()[-1] != "l"):
            new2 = deepcopy(currBoard)
            new2.move("r")
            moveProgress(new2,currBoard.getprev_path(),"r",PQ,node_created)
        
        # 3. Raising child node based on move Down
        x3, _ = currBoard.getBlank()
        if (x3 != 3) and (currBoard.getprev_path()[-1] != "u"):
            new3 = deepcopy(currBoard)
            new3.move("d")
            moveProgress(new3,currBoard.getprev_path(),"d",PQ,node_created)
        
        # 4. Raising child node based on move Down
        _, y4 = currBoard.getBlank()
        if (y4 != 0) and (currBoard.getprev_path()[-1] != "r"):
            new4 = deepcopy(currBoard)
            new4.move("l")
            moveProgress(new4,currBoard.getprev_path(),"l",PQ,node_created)
            
    stop = time.time()
    timeTaken = (stop-start)*1.00
    
    print()
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("INITIAL STATE PUZZLE-15:")
    board.printMatrix()
    
    i = 0
    for direction in PQ[0][1].getprev_path():
        if i == 0:
            i += 1
            continue
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        print("LANGKAH yg DIAMBIL : ",end="")
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
        board.printMatrix()

    print(f"Waktu eksekusi program: {timeTaken}")
    print(f"Banyaknya simpul yang dibangkitkan (simpul hidup): {node_created.count}")


