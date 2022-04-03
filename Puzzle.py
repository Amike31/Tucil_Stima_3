class Puzzle():
    
    def __init__(self):
        self.mat  = [[0 for j in range(4)] for i in range(4)]
        self.kur  = [0 for i in range(16)]
        self.blankX = 0
        self.blankY = 0
        
    # def __init__(self, mat, kurang, blank):   gimana cara .. ctor user-defined??
    #     self.mat = mat
    #     self.kur = kurang
    #     self.blank = blank
    
    def makeMatrix(self):
        self.readMatrix()
        self.fillKURANGI()
    
    def fillKURANGI(self):
        for i in range(4):
            for j in range(4):
                # pos1 dan pos2 dalam rentang 1<= x <=16
                pos1 = (i)*4 + (j+1)
                temp = self.mat[i][j]
                # Cek selanjutnya : J < I dan POSISI(J) > POSISI(I)
                for k in range(4):
                    for l in range(4):
                        pos2 = (k)*4 + (l+1)
                        if pos2 > pos1:
                            if self.mat[k][l] < temp:
                                self.kur[temp-1] += 1
                                
    def BOUNDING(self):
        sum = 0
        for i in range(16):
            sum += self.kur[i]
            
        # Jika pada daerah diarsir
        if (self.blankX+self.blankY)%2 == 1:
            sum += 1
        return sum%2==0
                                
    def readMatrix(self):
        print("Masukkan matrix 16 angka (dalam bentuk kotak dg spasi)")
        for i in range(4):
            word = input()
            self.mat[i] = [int(x) for x in word.split()]
            for j in range(4):
                if self.mat[i][j]==16:
                    self.blankX = i
                    self.blankY = j
    
    def printMatrix(self):
        print("Masukkan matrix 16 angka")
        for i in range(4):
            for j in range(4):
                print(self.mat[i][j], end=" ")
            print()
    
    def printBlankLocation(self):
        print("Blank ada di {}".format(self.blank))
    
    def printKURANGI(self):
        for i in range(16):
            print("angka ke-{} : {}".format(i+1,self.kur[i]))

a = Puzzle()
a.readMatrix()
a.printMatrix()
a.fillKURANGI()
print()
a.printKURANGI()
print(f"Bisa? {a.BOUNDING()}")