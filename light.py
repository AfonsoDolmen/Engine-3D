import math

class Light:
    def __init__(self):
        # The color of the light it has to be only 0.1
        # Else, if the color is > when 0.1, the renderer it's not gonna work
        self.color_light = [1,1,1]

    # Create the ambient light
    def ambient_light(self,ambient_strenght,object_color):        
        self.ambient = [self.color_light[0] * ambient_strenght,
                        self.color_light[1] * ambient_strenght,
                        self.color_light[2] * ambient_strenght]

        self.ambient_result = [object_color[0] * self.ambient[0],
                               object_color[1] * self.ambient[1],
                               object_color[2] * self.ambient[2]]

        return self.ambient_result

    def diffuse_light(self,normal,object_color,light_position,light_pos,ambient):
        self.light_dir = [light_position[0][0] - light_pos[0][0],
                          light_position[0][1] - light_pos[0][1],
                          light_position[0][2] - light_pos[0][2]]

        self.light_dir_mag = (self.light_dir[0]**2 + self.light_dir[1]**2 + self.light_dir[2]**2)
        self.light_dirN = [self.light_dir[0] / self.light_dir_mag,
                           self.light_dir[1] / self.light_dir_mag,
                           self.light_dir[2] / self.light_dir_mag]

        self.diff_dot = self.light_dirN[0] * normal[0] + self.light_dirN[1] * normal[1] + self.light_dirN[2] * normal[2]
        self.diff     = max(self.diff_dot,0.0)

        self.diffuse = [self.diff * self.color_light[0],
                        self.diff * self.color_light[1],
                        self.diff * self.color_light[2]]

        self.diffuseAmbient = [ambient[0] * self.diffuse[0],
                               ambient[1] * self.diffuse[1],
                               ambient[2] * self.diffuse[2]]

        self.diffuse_result = [self.diffuseAmbient[0] * object_color[0],
                               self.diffuseAmbient[1] * object_color[1],
                               self.diffuseAmbient[2] * object_color[2]]

        return self.diffuse_result