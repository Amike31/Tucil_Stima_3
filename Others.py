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




