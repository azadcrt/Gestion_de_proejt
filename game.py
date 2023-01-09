import sys
import numpy as np
import time
import pygame

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
    if x=="STOP" or y=="STOP":
        quit()
    else:
        if x=='UNDO' or y=='UNDO':
            Joue(taille, None, m//taille, m%taille, mat, None)
        else:
            if(len(x)==2 and len(y)==2):
                x=int(x)
                y=int(y)
                if (mat[x][y]!=None and z!=None) or (x<0 or x>=taille or y<0 or y>=taille):
                    del x
                    del y
                    time.sleep(10)
                    filin = open("test", "r")
                    lignes = filin.readlines()
                    x=str(lignes[0])
                    if len(lignes)==2:
                        y=str(lignes[1])
                    else:
                        y=None
                    Joue(taille,z,x,y,mat,m)
                else:
                    mat[x][y]=z
            else:
                del x
                del y
                time.sleep(10)
                filin = open("test", "r")
                lignes = filin.readlines()
                x=str(lignes[0])
                if len(lignes)==2:
                    y=str(lignes[1])
                else:
                    y=None
                Joue(taille,z,x,y,mat,m)

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
    pygame.draw.circle(screen, (0, 0, 255), (posy , posx ), (x/4))

def lect(nbcol, indexx,indexy):
    gap=ws/nbcol
    locx=(gap*indexx)+(gap/2)
    locy=(gap*indexy)+(gap/2)
    loctab = [None] * 3
    loctab[0] = locx
    loctab[1] = locy
    loctab[2] = gap
    return loctab




if(len(sys.argv)<3):
    print('Mauvais usage du jeu : python3 nomfichier taillePlateau coupParTour')
    quit()
if(int(sys.argv[1])<3):
    print('Mauvais usage du jeu : premier argument supérieur ou égal à 3')
    quit()
if(int(sys.argv[2])>2 or int(sys.argv[2])<0):
    print('Mauvais usage du jeu : deuxième argument supérieur égal à 1 ou 2')
    quit()

pygame.init()
ws = 600
screen = pygame.display.set_mode([ws, ws])

turn=0
memory=0
nbplay=1
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
    
    filin = open("test", "r")
    lignes = filin.readlines()
    c1=str(lignes[0])
    if len(lignes)==2:
        c2=str(lignes[1])
    else:
        c2=None

    print(mat)
    checkWin(rows,mat)
    
    if(nbplay<int(sys.argv[2])):
        nbplay=nbplay+1
    else:
        turn=(turn+1)%2
        nbplay=1
        
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