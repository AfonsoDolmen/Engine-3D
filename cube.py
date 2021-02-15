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

    def triangles(self):
        # Creating the list of triangles
        
                        # Frontal face
        self.triangles=[[0,1,3],
                        [1,2,3],
                        
                        # Left face
                        [0,4,5], 
                        [5,1,0],
                        
                        # Back face
                        [4,5,7],
                        [5,6,7],
                        
                        # Right face
                        [7,6,2],
                        [2,3,7],
                        
                        # Top face
                        [1,5,6],
                        [6,2,1],
                        
                        # Bottom face
                        [0,4,7],
                        [7,3,0]]

        return self.triangles
