import pygame

class Cube:
    def vertices(self):
        # Creating the list with the vertices
        vertices = [n for n in range(8)]

        # Assigning the vertices
        vertices[0] = [0,0,0]
        vertices[1] = [0,1,0]
        vertices[2] = [1,1,0]
        vertices[3] = [1,0,0]

        vertices[4] = [0,0,1]
        vertices[5] = [0,1,1]
        vertices[6] = [1,1,1]
        vertices[7] = [1,0,1]

        return vertices

    def draw(self,screen,vertices):
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
