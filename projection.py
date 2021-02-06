import math, pygame

class Projection:
    def __init__(self):
        self.i = 0
        
    def multiply(self, vertices, matrix, proj_v):
        # Multiplying the vertices
        self.x = vertices[self.i][0] * matrix[0][0] + vertices[self.i][1] * matrix[0][1] + vertices[self.i][2] * matrix[0][2] + matrix[0][3]
        self.y = vertices[self.i][0] * matrix[1][0] + vertices[self.i][1] * matrix[1][1] + vertices[self.i][2] * matrix[1][2] + matrix[1][3]
        self.z = vertices[self.i][0] * matrix[2][0] + vertices[self.i][1] * matrix[2][1] + vertices[self.i][2] * matrix[2][2] + matrix[2][3]
        self.w = vertices[self.i][0] * matrix[3][0] + vertices[self.i][1] * matrix[3][1] + vertices[self.i][2] * matrix[3][2] + matrix[3][3]

        if self.w != 0.0:
            self.x = self.x / self.w
            self.y = self.y / self.w
            self.z = self.z / self.w

        # Adjusting all the vertices in the screen
        # The projection returns coordinates valor of -1 and 1
        self.x += 1.0; self.y += 1.0

        self.x *= 0.5 * 800
        self.y *= 0.5 * 400

        # Saving the vertices in a list
        proj_v[self.i] = [self.x,self.y,self.z]

        if self.i == len(vertices)-1: self.i = 0
        self.i += 1