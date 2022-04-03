class Board():
    ### Atribut Member
    f_cost = 0
    blankX = -1
    blankY = -1
    prev_path = ["none"]
    
    ### CTOR
    def __init__(self, mat, f_cost):
        self.f_cost = f_cost
        self.mat  = mat
        self.searchBLANK()
        
    ### SETTER & GETTER
    # Matrix
    def setMatrix(self, mat):
        self.mat = mat
    def getMatrix(self):
        return self.mat
    
    # f_cost
    def setf_cost(self, f_cost):
        self.f_cost = f_cost    
    def getf_cost(self):
        return self.f_cost
    
    # blank number
    def setBlank(self, x, y):
        self.blankX = x
        self.blankY = y
    def getBlank(self):
        return self.blankX, self.blankY
    
    # previous path
    def getprev_path(self):
        return self.prev_path
    
    ### COST MODIFIER
    def G_cost(self):
        sum = 0
        for i in range(4):
            for j in range(4):
                pos = (i)*4 + (j+1)
                if self.mat[i][j] != 16:
                    if pos != self.mat[i][j]:
                        sum += 1
        return sum
        
    def Total_cost(self):
        return self.f_cost + self.G_cost()

    ### PREV PATH MODIFIER
    def cont_path(self, curr):
        self.prev_path.append(curr)
        
    
    ### Matrix MODIFIER
    # blank finder
    def searchBLANK(self):
        x = -1
        y = -1
        for i in range(4):
            for j in range(4):
                if self.mat[i][j] == 16:
                    x = i
                    y = j
        return x, y
    
    # MOVE
    def Move(self, dir):
        x = self.blankX
        y = self.blankY
        xn = -1
        yn = -1
        if dir == "u":
            xn = x
            yn = y-1
        elif dir == "r":
            xn = x+1
            yn = y
        elif dir == "d":
            xn = x
            yn = y+1
        elif dir == "l":
            xn = x-1
            yn = y
        temp = self.mat[xn][yn]
        self.mat[xn][yn] = 16
        self.mat[x][y] = temp
        self.setBlank(xn,yn)
    
    # OUTPUT
    def printMatrix(self):
        print("/--..--..--..--\\")
        for i in range(4):
            print("|", end="")
            for j in range(4):
                bil = self.mat[i][j]
                if bil != 16:
                    if bil < 10:
                        print(f" {bil}", end="")
                    else:
                        print(bil, end="")
                else:
                    print("  ", end="")
                if j!=3:
                    print("  ",end="")
                else:      
                    print("|")
        print("\\--..--..--..--/")
              
        
    ### CHECKING FUNCTION
    def KURANGI(self):
        KURANGI = [0 for i in range(16)]
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
                                KURANGI[temp-1] += 1
        return KURANGI
    
    def BOUNDING(self):
        KURANGI = self.KURANGI()
        sum = 0
        for i in range(16):
            sum += KURANGI[i]
            
        # Jika blank ada pada daerah diarsir
        if (self.blankX+self.blankY)%2 == 1:
            sum += 1
        return sum, sum%2==0        # int, bool  = {jumlah KURANG(i)+X, apakah genap}
    
    def isGOAL_STATE(self):
        for i in range(4):
            for j in range(4):
                pos = (i)*4 + (j+1)
                if (pos != self.mat[i][j]):
                    return False
        return True

    def printKURANGI(self):
        KURANGI = self.KURANGI()
        print("Tabel Nilai KURANGI: ")
        print("|-----------|")
        print("| ANGKA| N  |")
        print("|-----------|")
        for i in range(16):
            n = KURANGI[i]
            if i+1 < 10:
                if n < 10:
                    print(f"|   {i+1}  |  {KURANGI[i]} |")
                else:
                    print(f"|   {i+1}  | {KURANGI[i]} |")
            else:
                if n < 10:
                    print(f"|  {i+1}  |  {KURANGI[i]} |")
                else:
                    print(f"|  {i+1}  | {KURANGI[i]} |")
        print("|-----------|")
            
    # # // PRINT    
    # def printBlankLocation(self):
    #     print("Blank ada di {}".format(self.blank))
    
      

