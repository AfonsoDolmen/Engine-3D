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

        # Assigning the vertices
        # self.vertices[0] = [0,0,0]
        # self.vertices[1] = [0,1,0]
        # self.vertices[2] = [1,1,0]
        # self.vertices[3] = [1,0,0]

        # self.vertices[4] = [0,0,1]
        # self.vertices[5] = [0,1,1]
        # self.vertices[6] = [1,1,1]
        # self.vertices[7] = [1,0,1]

        return self.vertices
        
