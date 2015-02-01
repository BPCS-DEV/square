#! /usr/bin/python
import random

import curses


validValues=[2,2,4]

class square(object):
    
    def __init__(self,xspace,yspace):
        self.x=xspace
        self.y=yspace
        self.emptyCells=[] 
        self.moved=0
        arry=[]
        empty=[]
        for ycell in range(0,yspace):
            arrx=[]
            for xcell in range(0,xspace):
                empty.append([ycell,xcell])
                arrx.append(0)
            arry.append(arrx)

        self.emptyCells=empty
        
        #print arry[emptyCells[13][0]][emptyCells[13][1]]
        
        self.box=arry

    def checkEmptyCells(self):
        empty=[]
        A=self.box
        for ycell in range(0,self.y):
            for xcell in range(0,self.x):
                if A[ycell][xcell]==0:
                    empty.append([ycell,xcell])
                
            
        self.emptyCells=empty
        return len(empty)
        
        
    def tabletotext(self):
        o=""
        for i in self.box:
            o+=str(i)+"\n"
        stdscr.addstr(0, 0, o)
    
            
    def addentry(self):
        elementnumber=random.randint(0,len(self.emptyCells)-1)
        randombox=self.emptyCells[elementnumber]
        self.box[randombox[0]][randombox[1]]=getRandomNumber()
        del(self.emptyCells[elementnumber])
    
    
    def moveLeft(self,liste):
        m=0
        ll=len(liste)
        while True:
            if liste[m]==0:
                if liste[m+1]>0:
                    liste[m]=liste[m+1]
                    liste[m+1]=0
                    m=0
                    self.moved=1
            m+=1
            if m==ll-1:
                break
        return liste

    def uniteLeft(self,liste):
        m=0
        ll=len(liste)
        while True:
            if liste[m+1]==liste[m] and liste[m]>0:
                liste[m]=liste[m]*2
                liste[m+1]=0
                m=0
                self.moved=1
            m+=1
            if m==ll-1:
                break
        return liste
            
    

    def left(self):
        for i in range(0,len(self.box)):
            line=self.box[i]
            m=self.moveLeft(line)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            self.box[i]=m
  
    def right(self):
        for i in range(0,len(self.box)):
            line=self.box[i]
            line=self.inverteList(line)
            
            m=self.moveLeft(line)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            
            self.box[i]=self.inverteList(m)
            
    def up(self):
        zipped=[]
        for i in zip(*self.box):
            i=list(i)
            #print i
            m=self.moveLeft(i)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            zipped.append(m)
        k=[]
        for i in zip(*zipped):
            k.append(list(i))
        
        for i in range(0,len(k)):
            self.box[i]=k[i]
        
            
    def down(self):
        zipped=[]
        for i in zip(*self.box):
            i=list(i)
            i=self.inverteList(i)
            m=self.moveLeft(i)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            zipped.append(self.inverteList(m))
            
        k=[]
        for i in zip(*zipped):
            k.append(list(i))
        
        for i in range(0,len(k)):
            self.box[i]=k[i]
            
        
    def inverteList(self,liste):
        return liste[::-1]
    
        
        
        
    
def getRandomNumber():
    return validValues[random.randint(0,len(validValues)-1)]


stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''




z=square(4,4)
z.addentry()
z.tabletotext()

while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        z.up()
        
        #stdscr.addstr(2, 20, "Up")
    elif key == curses.KEY_DOWN: 
        z.down()
        
        #stdscr.addstr(3, 20, "Down")
    elif key == curses.KEY_LEFT: 
        z.left()
    elif key == curses.KEY_RIGHT: 
        z.right()
    if z.checkEmptyCells() == 0:
        break
    
    if z.moved==1:
        z.addentry()
    z.moved=0
    z.tabletotext() 
    
    stdscr.refresh()

        

curses.endwin()


