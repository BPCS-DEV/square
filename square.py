#! /usr/bin/python
import random

import curses
import re


class square(object):
    def __dir__(self):
            return ['__init__', 'addentry', 'tabletotext']
        
    def __init__(self,xspace,yspace):
        self.x=xspace
        self.y=yspace
        self.emptyCells=[] 
        self.moved=0
        self.validValues=[2,2,4]

        arry=[]
        empty=[]
        for ycell in range(0,yspace):
            arrx=[]
            for xcell in range(0,xspace):
                arrx.append(0)
            arry.append(arrx)
        self.box=arry
        self.checkEmptyCells()

    def checkEmptyCells(self):
        empty=[]
        A=self.box
        for ycell in range(0,self.y):
            for xcell in range(0,self.x):
                if A[ycell][xcell]==0:
                    empty.append([ycell,xcell])
        self.emptyCells=empty
        return len(empty)
        
        
            
    def addentry(self):
        elementnumber=random.randint(0,len(self.emptyCells)-1)
        randombox=self.emptyCells[elementnumber]
        self.box[randombox[0]][randombox[1]]=self.getRandomNumber()
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
      
    
    def moveHori(self,direction):
        for i in range(0,len(self.box)):
            m=self.box[i]
                     
            if direction == "right":
                m=self.inverteList(m)        
            
            m=self.moveLeft(m)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            
            if direction == "right":
                m=self.inverteList(m)        
            
            self.box[i]=m
     
    def moveVert(self,direction):
        zipped=[]
        for i in zip(*self.box):
            i=list(i)
            if direction == "down":
                i=self.inverteList(i)
            m=self.moveLeft(i)
            m=self.uniteLeft(m)
            m=self.moveLeft(m)
            if direction == "down":
                zipped.append(self.inverteList(m))
            else:
                zipped.append(m)
            k=[]
            for i in zip(*zipped):
                k.append(list(i))
        for i in range(0,len(k)):
            self.box[i]=k[i]
    
        
    def inverteList(self,liste):
        return liste[::-1]
    
    def getRandomNumber(self):
        return self.validValues[random.randint(0,len(self.validValues)-1)]

    def tabletotext(self):
        o="\n."+"."*11*self.x+"\n:"
        for i in self.box:
            f=" "*10+":"
            o+=f*4+"\n:"
            for e in i:
                o+="{:^10s}".format(str(e))+":"
            o+="\n:"+f*4+"\n"
            o+=":"+"."*11*self.x+"\n:"
        o= re.sub(" 0 ", "   ", o)
        o=o[:-1]
        return o


def main():
    stdscr = curses.initscr()


    z=square(4,4)  # build internal structure
    z.addentry()   # add first random entry
    stdscr.addstr(0, 0, z.tabletotext()) # print
    
    curses.cbreak() 
    stdscr.keypad(1)

    stdscr.addstr(0,10,"Hit 'q' to quit")
    stdscr.refresh()

    key = ''
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.addch(20,25,key)
        stdscr.refresh()
        if key == curses.KEY_UP: 
            z.moveVert("up")
        elif key == curses.KEY_DOWN: 
            z.moveVert("down")
        elif key == curses.KEY_LEFT: 
            z.moveHori("left")
        elif key == curses.KEY_RIGHT: 
            z.moveHori("right")
        if z.checkEmptyCells() == 0:
            break

        if z.moved==1:
            z.addentry()
        z.moved=0
        stdscr.addstr(0, 0, z.tabletotext()) # print

        stdscr.refresh()
    curses.endwin()

if __name__=="__main__":
    main()




