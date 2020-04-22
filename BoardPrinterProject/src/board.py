# Place your Board class in this file
from typing import *

class Board(object):
    def __init__(self,name:str,row:int,col:int,fill:str)->None:
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

        fillboard()
        showboard()

    def fillboard(self):
        pass


    def showboard
        pass

