from array import Array
from calendar import c
from re import I

from soupsieve import select

class Cube(object):
    def __init__(self, rows, cols, depth, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array[cols]
            for col in range(cols):
                self.data[row][col] = Array(depth, fill_value)
                
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        resutl = ""
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    resutl += str(self.data[row][col][depth])
                    
                resutl += "\n"
        return str(resutl)
