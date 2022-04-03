from copy import deepcopy
import random

def readFile(filename):
    filename = "test/" + filename
    with open(filename, 'r') as f:
        mat = [[int(num) for num in line.split(' ')] for line in f if line.strip() != "" ]
    return mat

def readManual():
    print("Masukkan matrix 16 angka (dalam bentuk kotak dg spasi): ")
    mat = [[0 for j in range(4)] for i in range(4)]
    for i in range(4):
        word = input()
        mat[i] = [int(x) for x in word.split()]
    return mat

def randomize():
    mat = random.sample(range(1,17),16)
    return mat

def isGOAL_STATE(mat):
    for i in range(4):
        for j in range(4):
            pos = (i)*4 + (j+1)
            if (pos != mat[i][j]):
                return False
    return True

# Fungsi untuk menentukan simpul yang diexpand dan yang dimasukkan ke dalam antria
def moveProgress(thisBoard, prev_Path, nextDirection, PQ, node_created):
    thisBoard.incrementf_cost()
    thisBoard.prev_path = deepcopy(prev_Path)
    thisBoard.continue_path(nextDirection)
    this_cost = thisBoard.Total_cost()
    PQ.append( (this_cost, thisBoard) )
    node_created.count = node_created.count + 1
    # print(node_created.count)

# def sorting(PQ):
#     newPQ = []
#     Elm1 = PQ[0]
#     PQ.pop(0)
#     while len(PQ)>0:
#         if 
    
    