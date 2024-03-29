from copy import deepcopy
import random

def readFile(filename):
    filename = "test/" + filename +".txt"
    try:
        with open(filename, 'r') as f:
            mat = [[int(num) for num in line.split(' ')] for line in f if line.strip() != "" ]
        return mat
    except FileNotFoundError:
        return [-1]

def readManual():
    print("Masukkan matrix 16 angka (dalam bentuk kotak dg spasi): ")
    mat = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        word = input()
        mat[i] = [int(x) for x in word.split()]
    return mat

def bigRandomize():
    ran = random.sample(range(1,17),16)
    mat = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            mat[i][j] = int(ran[4*i + j])
    return mat

def simpleRandomize():
    ran = random.sample(range(12,17),5)
    mat = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            pos = (i*4 + j)
            if pos < 11:
                mat[i][j] = pos+1
            else:
                mat[i][j] = int(ran[pos-11])
    return mat

def isGOAL_STATE(mat):
    for i in range(4):
        for j in range(4):
            pos = (i)*4 + (j+1)
            if (pos != mat[i][j]):
                return False
    return True
    
# Fungsi untuk menentukan simpul yang diexpand dan yang dimasukkan ke dalam antrian
def moveProgress(thisBoard, prev_Path, nextDirection, PQ, node_created):
    thisBoard.incrementf_cost()
    thisBoard.prev_path = deepcopy(prev_Path)
    thisBoard.continue_path(nextDirection)
    this_cost = thisBoard.Total_cost()
    # PQ.append( (this_cost, thisBoard) )                           # LIST IMPLEMENT
    PQ.put( (this_cost, thisBoard) )                                # Prio IMPLEMENT
    node_created.count = node_created.count + 1
    
# def printM(mat):
#     for i in range(4):
#         for j in range(4):
#             print(mat[i][j],end=" ")
#         print()

# mat = simpleRandomize()
# printM(mat)
