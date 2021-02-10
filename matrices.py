import math

class Matrix:
    def projection_matrice(self,near,far,fov):
        self.near = near
        self.far = far
        self.fov = fov
        self.a = 400/800

        self.m00 = 1.0 / self.a * math.tan(self.fov/2)
        self.m11 = 1.0 / math.tan(self.fov/2)
        self.m22 = (self.far + self.near) / (self.far - self.near)
        self.m23 = (2 * self.far * self.near) / (self.far - self.near)

        self.projection_matrix = [[self.m00,0,0,0],
                                  [0,self.m11,0,0],
                                  [0,0,-self.m22,-self.m23],
                                  [0,0,-1,0]]

        return self.projection_matrix

    def rotation_matrixX(self,angle):
        self.angle = angle

        self.rotationX = [[1,0,0,0],
                        [0,math.cos(self.angle),-math.sin(self.angle),0],
                        [0,math.sin(self.angle),math.cos(self.angle),0],
                        [0,0,0,1]]
        
        return self.rotationX

    def rotation_matrixY(self,angle):
        self.angle = angle

        self.rotationY = [[math.cos(self.angle),0,math.sin(self.angle),0],
                        [0,1,0,0],
                        [-math.sin(self.angle),0,math.cos(self.angle),0],
                        [0,0,0,1]]
        
        return self.rotationY

    def rotation_matrixZ(self,angle):
        self.angle = angle

        self.rotationZ = [[math.cos(self.angle),math.sin(self.angle),0,0],
                         [-math.sin(self.angle),math.cos(self.angle),0,0],
                         [0,0,1,0],
                         [0,0,0,1]]
        
        return self.rotationZ

    def translation_matrix(self,tX,tY,tZ):
        self.tX = tX
        self.tY = tY
        self.tZ = tZ

        self.translate = [[1,0,0,self.tX],
                          [0,1,0,self.tY],
                          [0,0,1,self.tZ],
                          [0,0,0,1]]

        return self.translate