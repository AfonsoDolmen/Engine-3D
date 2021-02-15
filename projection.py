import math, pygame

class Projection:
    def __init__(self):
        self.i  = 0
        
    def multiply(self, vertices, matrix, proj_v):
        while self.i < len(vertices):
            # Multiplying the vertices
            self.x = vertices[self.i][0] * matrix[0][0] + vertices[self.i][1] * matrix[0][1] + vertices[self.i][2] * matrix[0][2] + matrix[0][3]
            self.y = vertices[self.i][0] * matrix[1][0] + vertices[self.i][1] * matrix[1][1] + vertices[self.i][2] * matrix[1][2] + matrix[1][3]
            self.z = vertices[self.i][0] * matrix[2][0] + vertices[self.i][1] * matrix[2][1] + vertices[self.i][2] * matrix[2][2] + matrix[2][3]
            self.w = vertices[self.i][0] * matrix[3][0] + vertices[self.i][1] * matrix[3][1] + vertices[self.i][2] * matrix[3][2] + matrix[3][3]

            
            # Normalizing the vertices
            if self.w != 0.0:
                self.x = self.x / self.w
                self.y = self.y / self.w
                self.z = self.z / self.w

            proj_v[self.i] = [self.x,self.y,self.z]

            self.i += 1
        
        self.i = 0

    def draw(self,screen,vertices,triangles):
        while self.i < len(vertices):
            # Adjusting the coordinates of the vertices in the screen
            vertices[self.i][0] += 1; vertices[self.i][1] += 1

            vertices[self.i][0] *= 0.5 * 800
            vertices[self.i][1] *= 0.5 * 400

            self.i += 1

        self.i = 0

        # Drawing the triangles
        for triangle in triangles:
            a = triangle[0]
            b = triangle[1]
            c = triangle[2]

            pygame.draw.line(screen,(255,255,255),(vertices[a][0],vertices[a][1]),(vertices[b][0],vertices[b][1]))
            pygame.draw.line(screen,(255,255,255),(vertices[b][0],vertices[b][1]),(vertices[c][0],vertices[c][1]))
            pygame.draw.line(screen,(255,255,255),(vertices[c][0],vertices[c][1]),(vertices[a][0],vertices[a][1]))