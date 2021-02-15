# Projecting perspective 3D graphics.
# Programmed by Afonso ^^

# Futures updates:
# Culling;
# Rasterization;
# Clipping;
# And more!

import pygame
import projection,matrices,cube#,objLoader
import time
import math

# Create the screen
screen = pygame.display.set_mode((800,400))

# Summoning the objects
projection1 = projection.Projection()
matrix = matrices.Matrix()

# Summoning the object loader
# objLoader = objLoader.ObjLoader()

# Creating the cube with the position
cube = cube.Cube()
camera = [0,0,0]

# Taking the vertices of the cube
cubeVertices = cube.vertices()

clock = pygame.time.Clock()

index = 0

def update():
    index = 0
    angle = 0

    #vertices = objLoader.loadObj('lanterna.obj')

    #print(vertices)

    # Saving all the projected vertices in a list
    projected_vertices  = [n for n in range(len(cubeVertices))]

    rot_verticesX = [x for x in range(len(cubeVertices))]
    rot_verticesY = [y for y in range(len(cubeVertices))]
    rot_verticesZ = [f for f in range(len(cubeVertices))]

    translated_vertices = [m for m in range(len(cubeVertices))]
    scaled_vertices     = [s for s in range(len(cubeVertices))]

    # Taking the triangles
    triangles = [[0,1,3],   # Frontal face
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

    # Cube position
    tX,tY,tZ = 0, -0.5, 3

    # Cube scale
    scaleX,scaleY,scaleZ = 1, 0.8, 1
 
    # Taking the projection matrix
    projection_matrix = matrix.projection_matrice(0.1,1000,45)

    def scaleVertices(vertices,scaleMatrix,scaledVertices):
        for scaling in vertices:
            projection1.multiply(vertices,scaleMatrix,scaledVertices)

    def rotateVertices(vertices,rotationMatrix,rotatedVertices):
        for rotate in vertices:
            projection1.multiply(vertices,rotationMatrix,rotatedVertices)

    def translateVertices(vertices,translationMatrix,translatedVertices):
        for translate in vertices:
            projection1.multiply(vertices,translationMatrix,translatedVertices)
    
    def projectVertices(vertices,projectionMatrix,projectedVertices):
        for project in vertices:
            projection1.multiply(vertices,projectionMatrix,projectedVertices)

    # Principal loop
    while(True):
        fps = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # Clear the screen
        screen.fill((0,0,0))

        # Creating the matrices
        rotationX = matrix.rotation_matrixX(angle)
        rotationY = matrix.rotation_matrixY(angle)
        rotationZ = matrix.rotation_matrixZ(angle)
        translation = matrix.translation_matrix(tX,tY,tZ)
        scale = matrix.scale_matrix(scaleX,scaleY,scaleZ)

        # Multiplying the vertices by the matrices

        scaleVertices(cubeVertices,scale,scaled_vertices)
        rotateVertices(scaled_vertices,rotationY,rot_verticesY)
        translateVertices(rot_verticesY,translation,translated_vertices)
        projectVertices(translated_vertices,projection_matrix,projected_vertices)

        # Drawing the cube
        projection1.draw(screen,projected_vertices,triangles)

        angle -= 0.01
        # #scaleY    += 0.01

        # Updating the screen
        pygame.display.update()
    
    exit()

# Main function
def main():
    # Initializing PyGame
    pygame.init()

    # Update function
    update()

main()