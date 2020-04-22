# Place your Board class in this file
from typing import *

class Board:
    def __init__(self,name,row,col,fill):
    """
    Param
    """
        self.row = input('Enter the number of rows for your board:')
        self.col = input('Enter the number of columns for your board:')
        self.blank = input('Enter the blank character to be used on your board')

    def showboard