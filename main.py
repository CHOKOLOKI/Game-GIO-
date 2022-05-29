from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

duwa = Ursina()
Sky(texture='sky_sunset')
Tao = FirstPersonController()

class kahon(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='grass',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                ibutang = kahon(position=self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)

    #def menu():
        
#class Hand(Entity):
    #def __init__(self):
        #super().__init__(
            #parent = camera.ui,
            #model = 'assets/sword',
            #scale = 0.2,
            #rotation = Vec3(15,-10,0),
            #position = Vec2(0.4,-0.6))


for z in range(30):
    for x in range(30):
        ibutang = kahon(position=(x, 0, z))

hand = Hand()
duwa.run()
