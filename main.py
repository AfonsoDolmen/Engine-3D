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
cube = cube.Cube(0, 0, 3)
camera = [0,0,0]

# Taking the vertices of the cube
cubeVertices = cube.vertices()

clock = pygame.time.Clock()

index = 0

def update():
    index = 0
    angle = 0

    # Saving all the projected vertices in a list
    projected_vertices  = [n for n in range(len(cubeVertices))]

    rot_verticesX = [x for x in range(len(cubeVertices))]
    rot_verticesY = [y for y in range(len(cubeVertices))]
    rot_verticesZ = [f for f in range(len(cubeVertices))]

    translated_vertices = [m for m in range(len(cubeVertices))]

    triangles = [f for f in range(len(cubeVertices))]

    # Taking the projection matrix
    projection_matrix = matrix.projection_matrice(0.1,1000,45)

    tX,tY,tZ = 0, 0, 0

    #print(triangles)

    # Principal loop
    while(True):
        #fps = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # Clear the screen
        screen.fill((0,0,0))

        # Creating the matrices
        rotationX = matrix.rotation_matrixX(angle)
        rotationZ = matrix.rotation_matrixZ(angle)
        translation = matrix.translation_matrix(tX,tY,tZ)

        # Multiplying the vertices by the matrices
        # Rotating the vertices around the X axis
        for rotX in cubeVertices:
            projection1.multiply(cubeVertices,rotationX,rot_verticesX)

        # Rotating the vertices around the Z axis
        for rotZ in rot_verticesX:
            projection1.multiply(rot_verticesX,rotationZ,rot_verticesZ)

        # Translating the vertices
        for translate in rot_verticesZ:
            projection1.multiply(rot_verticesZ,translation,translated_vertices)

        # Finding the 3D object position in a 2D position
        for proj in translated_vertices:
            projection1.multiply(translated_vertices,projection_matrix,projected_vertices)

        # Taking the triangles coordinates
        while index < len(triangles):
            triangles[index] = [projected_vertices[0], projected_vertices[1], projected_vertices[2]]

            index += 1

        index = 0

        # Drawing the cube
        projection1.draw(screen,projected_vertices)

        angle += 0.003
        
        # Moving the vertices in the X axis and Z axis
        tX = -0.3
        tZ =  3

        # Updating the screen
        pygame.display.update()
    
    exit()

# Main function
def main():
    # Initializing PyGame
    pygame.init()

    update()

main()