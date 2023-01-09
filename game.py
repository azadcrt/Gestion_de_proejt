import sys
import numpy as np
import time
import pygame

pygame.init()

ws = 600
screen = pygame.display.set_mode([ws, ws])


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
    for i in range(2,x-1):
        for j in range(0,x-2):
            if mat[i][j] != None:
                m1 = mat[i][j]
                m2 = mat[i-1][j+1]
                m3 = mat[i-2][j+2]
                if m1==m2 and m1==m3:
                    return mat[i][j]

    for i in range(0,x-3):
        for j in range(0,x-3):
            if mat[i][j] != None:
                m1 = mat[i][j]
                m2 = mat[i+1][j+1]
                m3 = mat[i+2][j+2]
                if m1==m2 and m1==m3:
                    print(i,j)
                    return mat[i][j]
    
    return -1

def checkWin(x,mat):
    winner = ColWin(x,mat)
    if winner != -1:
        print("Le gagnant col est :", winner)
        quit()

    winner = RowWin(x,mat)
    if winner != -1:
        print("Le gagnant row est :", winner)
        quit()

    winner = checkDiagonals(x, mat)
    if winner != -1:
        print("Le gagnant diag est :", winner)
        quit()



def Joue(taille, z, x, y, mat, m):
    print(x)
    print(y)
    if x=="STOP" or y=="STOP":
        quit()
    else:
        if x=='UNDO' or y=='UNDO':
            Joue(taille, None, m//taille, m%taille, mat, None)
        else:
            x=int(x)
            y=int(y)
            if (mat[x][y]!=None and z!=None) or (x<0 or x>=taille or y<0 or y>=taille):
                time.sleep(10)
                filin = open("test", "r")
                lignes = filin.readlines()
                x=str(lignes[0])
                if len(lignes)==2:
                    x=str(lignes[1])
                else:
                    x=None
                Joue(taille,z,x,y,mat,m)
            else:
                mat[x][y]=z

def End(taille):
    for i in range(0, taille):
        for j in range(0, taille):
            if mat[i][j]==None:
                return 0
    return -1

def grill(x):
    i=0
    while i<x:
        pygame.draw.line(screen, (0,0,0), ((ws/x)*(i+1),0), ((ws/x)*(i+1),600), 2)
        pygame.draw.line(screen, (0,0,0), (0,(ws/x)*(i+1)), (600,(ws/x)*(i+1)), 2)
        i=i+1

def cross(posx,posy,x):
    pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx + (x/4)), (posy + (x/4) ,posx - (x/4)), int((x/4)))
    pygame.draw.line(screen, (255,0,0),(posy + (x/4) ,posx - (x/4)), (posy - (x/4) ,posx + (x/4)), int((x/4)))
    pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx - (x/4)), (posy + (x/4) ,posx + (x/4)), int((x/4)))
    pygame.draw.line(screen, (255,0,0),(posy - (x/4) ,posx - (x/4)), (posy + (x/4) ,posx + (x/4)), int((x/4)))
        
def circle(posx,posy,x):
    pygame.draw.circle(screen, (0, 0, 255), (posx , posy ), (x/4))

def lect(nbcol, indexx,indexy):
    gap=ws/nbcol
    locx=(gap*indexx)+(gap/2)
    locy=(gap*indexy)+(gap/2)
    loctab = [None] * 3
    loctab[0] = locx
    loctab[1] = locy
    loctab[2] = gap
    return loctab




turn=0
memory=0
if(len(sys.argv)<2):
    print('Mauvais usage du jeu : python3 nomfichier taillePlateau coupParTour')
    quit()
for i in range(1, len(sys.argv)):
    print('argument:', i, 'value:', sys.argv[i])
rows = int(sys.argv[1])
cols = int(sys.argv[1])
taille = rows*cols
mat = np.array([None]*taille).reshape(rows,cols)
while End(rows)==0:
    screen.fill((255, 255, 255))
    filin = open("test", "r")
    lignes = filin.readlines()
    c1=str(lignes[0])
    
    if len(lignes)==2:
        c2=str(lignes[1])
    else:
        c2=None
    Joue(rows, turn, c1, c2, mat, memory)
    print(mat)
    checkWin(rows,mat)
    turn=(turn+1)%2
    if c1=='UNDO' or c2=='UNDO':
        memory=None
    else:
        memory=int(c1)*rows+int(c2)

    loctab = lect(cols,0,0)
    grill(int(ws/loctab[2]))
    for i in range(0,rows):
        for j in range(0,cols):
            loctab = lect(cols,i,j)
            if(mat[i][j]==0):
                cross(loctab[0],loctab[1],loctab[2])
            if(mat[i][j]==1):
                circle(loctab[0],loctab[1],loctab[2])
    
   
    

    # Flip the display

    pygame.display.flip()
    time.sleep(10)
print('égalité')
pygame.quit()
quit()
#mat = [[0,2,7,4,5],[7,7,7,8,9],[7,11,7,12,13],[0,0,52,0,0], [0,0,52,0,0]]