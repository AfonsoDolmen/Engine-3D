import pygame

class Cube:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def vertices(self):
        # Creating the list with the vertices
        self.vertices = [[0,0,0],
                         [0,1,0],
                         [1,1,0],
                         [1,0,0],
                         
                         [0,0,1],
                         [0,1,1],
                         [1,1,1],
                         [1,0,1]]


        return self.vertices
        
