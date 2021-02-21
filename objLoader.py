class ObjLoader:
    def __init__(self, render):
        self.render = render

        self.i = 0

    def takeTriangles(self):
        return self.triangles

    def takeVertices(self):
        return self.vertices

    def loadObj(self, obj):
        # Opening the obj file
        o = open(obj, 'r')

        self.vertices  = []
        self.triangles = []

        for line in o:
            values = line.split()

            if line.startswith('#'):continue

            # Taking the vertices
            if values[0] == 'v':
                self.vertices.append(values[1:4])

            # Taking the triangles
            if values[0] == 'f':
                self.triangles.append(values[1:4])

        o.close()