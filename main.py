# Projecting perspective 3D graphics.
# Programmed by Afonso ^^

# Futures updates:
# Culling;
# Rasterization;
# Clipping;
# And more!

import pygame
import projection,matrices,cube
import time

# Create the screen
screen = pygame.display.set_mode((800,400))

# Summoning the objects
projection1 = projection.Projection()
matrix = matrices.Matrix()
cube = cube.Cube()

# Taking the vertices of the cube
cubeVertices = cube.vertices()

clock = pygame.time.Clock()

index = 0

# Moving all the vertices of the cube
for ver in cubeVertices:
    cubeVertices[index][0] -= 1.8   # X
    cubeVertices[index][1] -= 0.6   # Y
    cubeVertices[index][2] += 10    # Z

    index += 1

def update():
    angle = 0
    
    # Taking the projection matrix
    projection_matrix = matrix.projection_matrice(0.1,1000,90)

    # Saving all the projected vertices in a list
    projected_vertices = [n for n in range(len(cubeVertices))]

    while(True):
        fps = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # Clear the screen
        screen.fill((0,0,0))
        
        # Multiplying all the vertices by the projection matrix
        for x in cubeVertices:
            projection1.multiply(cubeVertices,projection_matrix,projected_vertices)

        # Drawing the cube
        cube.draw(screen,projected_vertices)

        # Updating the screen
        pygame.display.update()
    
    exit()

# Main function
def main():
    # Initializing PyGame
    pygame.init()

    update()

main()