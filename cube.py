import pygame

class Cube:
    def __init__(self):
        pass

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
        
