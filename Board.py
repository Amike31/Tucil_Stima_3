class Board():
    ### Atribut Member
    # f_cost : private
    # blankX : private
    # blankY : private
    # prev_path : private
    
    ### CTOR
    def __init__(self, mat):
        self.__f_cost = 0
        self.__mat  = mat
        self.__blankX, self.__blankY = self.searchBLANK()
        self.__prev_path = ["none"]
    ### CCTOR
    # Di python memakai fungsi deepcopy()
        
    ### SETTER & GETTER
    # Matrix
    def setMatrix(self, mat):
        self.__mat = mat
    def getMatrix(self):
        return self.__mat
    
    # f_cost
    def setf_cost(self, f_cost):
        self.__f_cost = f_cost  
    def getf_cost(self):
        return self.__f_cost
    
    # blank number
    def setBlank(self, x, y):
        self.__blankX = x
        self.__blankY = y
    def getBlank(self):
        return self.__blankX, self.__blankY
    
    # previous path
    def getprev_path(self):
        return self.__prev_path
    
    ### COST MODIFIER
    def incrementf_cost(self):
        self.__f_cost += 1
        
    def G_cost(self):
        sum = 0
        for i in range(4):
            for j in range(4):
                pos = (i)*4 + (j+1)
                if self.__mat[i][j] != 16:
                    if pos != self.__mat[i][j]:
                        sum += 1
        return sum
        
    def Total_cost(self):
        return self.__f_cost + self.G_cost()

    ### PREV PATH MODIFIER
    def continue_path(self, curr):
        self.__prev_path.append(curr)
        
    
    ### Matrix MODIFIER
    # blank finder
    def searchBLANK(self):
        x = -1
        y = -1
        for i in range(4):
            for j in range(4):
                if self.__mat[i][j] == 16:
                    x = i
                    y = j
        return x, y
    
    # MOVE
    def move(self, dir):
        x = self.__blankX
        y = self.__blankY
        # print(x,y)
        xn = -1
        yn = -1
        if dir == "u":
            xn = x-1
            yn = y
            # print(xn, yn)
        elif dir == "r":
            xn = x
            yn = y+1
        elif dir == "d":
            xn = x+1
            yn = y
        elif dir == "l":
            xn = x
            yn = y-1
        temp = self.__mat[xn][yn]
        self.__mat[xn][yn] = 16
        self.__mat[x][y] = temp
        self.setBlank(xn,yn)
    
    # OUTPUT
    def printMatrix(self):
        print("/--..--..--..--\\")
        for i in range(4):
            print("|", end="")
            for j in range(4):
                bil = self.__mat[i][j]
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
                temp = self.__mat[i][j]
                # Cek selanjutnya : J < I dan POSISI(J) > POSISI(I)
                for k in range(4):
                    for l in range(4):
                        pos2 = (k)*4 + (l+1)
                        if pos2 > pos1:
                            if self.__mat[k][l] < temp:
                                KURANGI[temp-1] += 1
        return KURANGI
    
    def BOUNDING(self):
        KURANGI = self.KURANGI()
        sum = 0
        for i in range(16):
            sum += KURANGI[i]
            
        # Jika blank ada pada daerah diarsir
        if (self.__blankX+self.__blankY)%2 == 1:
            sum += 1
        return sum, sum%2==0        # int, bool  = {jumlah KURANG(i)+X, apakah genap}
    

    def printKURANGI(self):
        KURANGI = self.KURANGI()
        print("Tabel Nilai KURANGI: ")
        print("|-----------|")
        print("| ANGKA|  N |")
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
            
    ### COMPARATOR (YA allah debug ini dari malem sampe 13 jam g tidur T_T)
    def __lt__(self, other):
        return True
    def __le__(self, other):
        return True
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True

