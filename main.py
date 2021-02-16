# Projecting perspective 3D graphics.
# Programmed by Afonso ^^

# Futures updates:
# Clipping;
# And more!

# Futures Added:
# Culling;
# Rasterization;

import pygame
import projection,matrices,cube,objLoader
import time
import math

# Summoning the objects
projection1 = projection.Projection()
matrix = matrices.Matrix()

# Summoning the object loader
objLoader = objLoader.ObjLoader(False)

objLoader.loadObj('teapot.obj')

# Taking the vertices and triangles of the obj
objVertices  = objLoader.takeVertices()
objTriangles = objLoader.takeTriangles()

cube = cube.Cube(False)

# Taking the vertices and triangles of the cube
cubeVertices  = cube.vertices()
cubeTriangles = cube.triangles()

clock = pygame.time.Clock()

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

def update(screen):
    index = 0
    angle = 0

    vertices  = cubeVertices.copy()
    triangles = cubeTriangles.copy()

    # Saving all the projected vertices in a list
    projected_vertices = [n for n in range(len(vertices))]

    rot_verticesX = [x for x in range(len(vertices))]
    rot_verticesY = [y for y in range(len(vertices))]
    rot_verticesZ = [f for f in range(len(vertices))]

    translated_vertices = [m for m in range(len(vertices))]
    scaled_vertices     = [s for s in range(len(vertices))]

    # Cube position
    tX,tY,tZ = 0, -0.7, 3

    # Cube scale
    scaleX,scaleY,scaleZ = 1, 0.7, 1
 
    # Taking the projection matrix
    projection_matrix = matrix.projection_matrice(0.1,1000,45)

    # Principal loop
    while(True):
        fps = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # Clear the screen
        screen.fill((0,0,0))

        # Creating the matrices
        rotationX   = matrix.rotation_matrixX(angle)
        rotationY   = matrix.rotation_matrixY(angle)
        rotationZ   = matrix.rotation_matrixZ(angle)
        translation = matrix.translation_matrix(tX,tY,tZ)
        scale       = matrix.scale_matrix(scaleX,scaleY,scaleZ)

        # Multiplying the vertices by the matrices
        scaleVertices(vertices,scale,scaled_vertices)
        rotateVertices(scaled_vertices,rotationY,rot_verticesY)
        translateVertices(rot_verticesY,translation,translated_vertices)
        projectVertices(translated_vertices,projection_matrix,projected_vertices)

        # Drawing the cube
        projection1.draw(screen,projected_vertices,triangles)

        # Subtracting the angle of the object
        angle -= 0.01

        # Updating the screen
        pygame.display.update()
    
    exit()

# Main function
def main():
    # Initializing PyGame
    pygame.init()

    # Create the screen
    screen = pygame.display.set_mode((800,400))

    # Update function
    update(screen)

main()