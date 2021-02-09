import math, pygame

class Projection:
    def __init__(self):
        self.i  = 0
        self.index = 0
        
    def multiply(self, vertices, matrix, proj_v):
        while self.i < len(vertices):
            # Multiplying the vertices
            self.x = vertices[self.i][0] * matrix[0][0] + vertices[self.i][1] * matrix[0][1] + vertices[self.i][2] * matrix[0][2] + matrix[0][3]
            self.y = vertices[self.i][0] * matrix[1][0] + vertices[self.i][1] * matrix[1][1] + vertices[self.i][2] * matrix[1][2] + matrix[1][3]
            self.z = vertices[self.i][0] * matrix[2][0] + vertices[self.i][1] * matrix[2][1] + vertices[self.i][2] * matrix[2][2] + matrix[2][3]
            self.w = vertices[self.i][0] * matrix[3][0] + vertices[self.i][1] * matrix[3][1] + vertices[self.i][2] * matrix[3][2] + matrix[3][3]

            
            # Adjusting all the vertices in the screen
            # The projection returns coordinates valor of -1 and 1
            if self.w != 0.0:
                self.x = self.x / self.w
                self.y = self.y / self.w
                self.z = self.z / self.w

            proj_v[self.i] = [self.x,self.y,self.z]

            self.i += 1
        
        self.i = 0

    def draw(self,screen,vertices):
        while self.index < len(vertices):
            vertices[self.index][0] += 1.0; vertices[self.index][1] += 1.0

            vertices[self.index][0] *= 0.5 * 800
            vertices[self.index][1] *= 0.5 * 400

            self.index += 1

        self.index = 0

        # Taking the position of the all the vertices
        a = vertices[0]
        b = vertices[1]
        c = vertices[2]
        d = vertices[3]

        e = vertices[4]
        f = vertices[5]
        g = vertices[6]
        h = vertices[7]

        # Front Face
        pygame.draw.line(screen,(255,255,255),(a[0],a[1]),(b[0],b[1]))
        pygame.draw.line(screen,(255,255,255),(b[0],b[1]),(d[0],d[1]))
        pygame.draw.line(screen,(255,255,255),(d[0],d[1]),(a[0],a[1]))
        pygame.draw.line(screen,(255,255,255),(b[0],b[1]),(c[0],c[1]))
        pygame.draw.line(screen,(255,255,255),(c[0],c[1]),(d[0],d[1]))

        # Left Face
        pygame.draw.line(screen,(255,255,255),(e[0],e[1]),(f[0],f[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(a[0],a[1]))
        pygame.draw.line(screen,(255,255,255),(a[0],a[1]),(e[0],e[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(b[0],b[1]))
        pygame.draw.line(screen,(255,255,255),(b[0],b[1]),(a[0],a[1]))

        # Right Face
        pygame.draw.line(screen,(255,255,255),(h[0],h[1]),(g[0],g[1]))
        pygame.draw.line(screen,(255,255,255),(g[0],g[1]),(d[0],d[1]))
        pygame.draw.line(screen,(255,255,255),(d[0],d[1]),(h[0],h[1]))
        pygame.draw.line(screen,(255,255,255),(g[0],g[1]),(c[0],c[1]))
        pygame.draw.line(screen,(255,255,255),(c[0],c[1]),(d[0],d[1]))

        # Back Face
        pygame.draw.line(screen,(255,255,255),(e[0],e[1]),(f[0],f[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(h[0],h[1]))
        pygame.draw.line(screen,(255,255,255),(h[0],h[1]),(e[0],e[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(g[0],g[1]))
        pygame.draw.line(screen,(255,255,255),(g[0],g[1]),(h[0],h[1]))

        # Top Face
        pygame.draw.line(screen,(255,255,255),(b[0],b[1]),(f[0],f[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(c[0],c[1]))
        pygame.draw.line(screen,(255,255,255),(c[0],c[1]),(b[0],b[1]))
        pygame.draw.line(screen,(255,255,255),(f[0],f[1]),(g[0],g[1]))
        pygame.draw.line(screen,(255,255,255),(g[0],g[1]),(c[0],c[1]))

        # Bottom Face
        pygame.draw.line(screen,(255,255,255),(a[0],a[1]),(e[0],e[1]))
        pygame.draw.line(screen,(255,255,255),(e[0],e[1]),(d[0],d[1]))
        pygame.draw.line(screen,(255,255,255),(d[0],d[1]),(a[0],a[1]))
        pygame.draw.line(screen,(255,255,255),(e[0],e[1]),(h[0],h[1]))
        pygame.draw.line(screen,(255,255,255),(h[0],h[1]),(d[0],d[1]))