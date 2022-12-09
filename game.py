import sys

def ColWin(x, mat):
    for i in range(0,x):
        for j in range(0,x-2):
            if mat[i][j] != None:
                if mat[i][j] == mat[i][j+1] and mat[i][j] == mat[i][j+2]:
                    return mat[i][j]
    return -1

def RowWin(x, mat):
    for i in range(0,x):
        for j in range(0,x-2):
            if mat[j][i] != None:
                if mat[j][i] == mat[j+1][i] and mat[j][i] == mat[j+2][i]:
                    return mat[j][i]
    return -1

def checkDiagonals(x, mat):
    for i in range(2,x-2):
        for j in range(0,x-2):
            if mat[j][i] != None:
                m1 = mat[i][j]
                m2 = mat[i-1][j+1]
                m3 = mat[i-2][j+2]
                if m1==m2 and m1==m3:
                    return mat[i][j]

    for i in range(0,x-2):
        for j in range(0,x-2):
            if mat[j][i] != None:
                m1 = mat[i][j]
                m2 = mat[i+1][j+1]
                m3 = mat[i+2][j+2]
                if m1==m2 and m1==m3:
                    return mat[i][j]
    
    return -1

def checkWin(x,mat):
    winner = ColWin(x,mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()

    winner = RowWin(x,mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()

    winner = checkDiagonals(x, mat)
    if winner != -1:
        print("Le gagnant est :", winner)
        quit()



def Joue(z, x, y, mat):
    if x=="STOP" or y=="STOP":
        quit()
    mat[x][y]=z

def End()

for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])

x = int(sys.argv[i])
mat = [[None]*x]*x
mat = [[0,2,7,4,5],[7,7,7,8,9],[7,11,7,12,13],[0,0,52,0,0], [0,0,52,0,0]]
print(mat)
checkWin(x,mat)