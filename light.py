class Light:
    def __init__(self):
        pass

    # Create the ambient light
    def ambient_light(self,ambient_strenght,object_color):
        # The color of the light it has to be only 0.1
        # Else, if the color is > when 0.1, the renderer it's not gonna work
        self.color_light = [0.1,0.1,0.1]

        self.ambient = [self.color_light[0] * ambient_strenght,
                        self.color_light[1] * ambient_strenght,
                        self.color_light[2] * ambient_strenght]

        self.result = [object_color[0] * self.ambient[0],
                       object_color[1] * self.ambient[1],
                       object_color[2] * self.ambient[2]]

        return self.result