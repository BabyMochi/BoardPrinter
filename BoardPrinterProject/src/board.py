# Place your Board class in this file
from typing import *

class Board(object):
    def __init__(self,name:str,row:int,col:int,fill:str,change:list)->None:
        """
        Param name
        Param row
        Param col
        Param what to fill with
        """
        self._name=name
        self._row=row
        self._col=col
        self._fill=fill
        self._change=change


        fillboard()
        firstline()
        showboard()

    def firstline(self):
        firstline=[" "]
        for i in range(0,self._col):
            firstline.append(i)

    def fillboard(self):
        self.listofboard=[]
        for i in range(0,self._row):
            self.listofboard.append(createlist())


        pass
    def createlist(self):
        return [self.fill for i in range(0,self._col)]


    def changespot(self):
        """
        :return:
        :rtype:
        """
        char=self._change[0]
        ypos=self.change[1]
        xpos = self.change[2]
        showboard()

    def showboard(self):
        print(self._name)
        print(*self.firstline)
        for ele,row in enumerate(self.listofboard)
            print(ele,*row)