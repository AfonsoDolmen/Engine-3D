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
import math

# Create the screen
screen = pygame.display.set_mode((800,400))

# Summoning the objects
projection1 = projection.Projection()
matrix = matrices.Matrix()

# Creating the cube with the position
cube = cube.Cube(1.5,0.5,3)
camera = [0,0,0]

# Taking the vertices of the cube
cubeVertices = cube.vertices()

clock = pygame.time.Clock()

index = 0

# Moving all the vertices of the cube
for v in cubeVertices:
    cubeVertices[index][0] -= cube.x   # X
    cubeVertices[index][1] -= cube.y   # Y
    cubeVertices[index][2] += cube.z   # Z

    index += 1

def update():
    index  = 0
    index1 = 1
    index2 = 2

    angle = 0

    # Saving all the projected vertices in a list
    projected_vertices = [n for n in range(len(cubeVertices))]
    rot_vertices = [f for f in range(len(cubeVertices))]

    triangles = [f for f in range(len(cubeVertices))]

    # Taking the projection matrix
    projection_matrix = matrix.projection_matrice(0.1,1000,45)

    for triangle in triangles:
        triangles[index] = [projected_vertices[0],projected_vertices[1],projected_vertices[2]]

        index += 1

    index = 0

    #print(triangles)

    # Principal loop
    while(True):
        #fps = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # Clear the screen
        screen.fill((0,0,0))

        # Culling
        v10 = [cubeVertices[1][0] - cubeVertices[0][0],
                cubeVertices[1][1] - cubeVertices[0][1],
                cubeVertices[1][2] - cubeVertices[0][2]]
        
        v20 = [cubeVertices[2][0] - cubeVertices[0][0],
                cubeVertices[2][1] - cubeVertices[0][1],
                cubeVertices[2][2] - cubeVertices[0][2]]

        n = [v10[0] * v20[0],
                v10[1] * v20[1],
                v10[2] * v20[2]]

        p = [cubeVertices[0][0] - camera[0],
                cubeVertices[0][1] - camera[1],
                cubeVertices[0][2] - camera[2]]

        pn = [p[1]*n[2] - p[2]*n[1],
                p[2]*n[0] - p[0]*n[2],
                p[0]*n[1] - p[1]*n[0]]

        
        # for proj1 in cubeVertices:
        #     projection1.multiply(cubeVertices,projection_matrix,projected_vertices)

        rotationZ = matrix.rotation_matrixZ(angle)

        for rot in cubeVertices:
            projection1.multiply(cubeVertices,rotationZ,rot_vertices)


        for proj in rot_vertices:
            projection1.multiply(rot_vertices,projection_matrix,projected_vertices)

        if pn[0] + pn[1] + pn[2] < 0:    
            projection1.draw(screen,projected_vertices)

        angle += 0.001

        # Updating the screen
        pygame.display.update()
    
    exit()

# Main function
def main():
    # Initializing PyGame
    pygame.init()

    update()

main()