from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


for z in range(10):
    for x in range(10):
        Entity(
            model="cube", color=color.dark_gray, collider="box", ignore=True,
            position=(x, 0 , z),
            parent=scene,
            origin_y = 0.5,
            texture = "white_cube"
        )


class TextureBox(Button):
    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="texture.png",
            color = color.color(0,0,1)
        )

        self.texture_choice = 0
        self.textures = ["texture.png", "wood.png", "stones.jpeg", "blue.jpg"]

    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.texture_choice += 1
                self.texture_choice %= len(self.textures)
                self.texture = self.textures[self.texture_choice]


class myPlayer(FirstPersonController):
    def __init__(self):
        super().__init__()

        myPlayer.fall_after = 0
    
    def input(self, key):
        if key == "left shift" == 1:
            myPlayer.speed = lerp(player.speed, run_speed, 0.01)
            print('jsdashfasd')
        else:
            myPlayer.speed = 5


TextureBox()

player = myPlayer()
#player = FirstPersonController()
#player.fall_after = 0
#player = Entity(model="cube", color=color.blue, scale_y=2)

velocity = 0.01
run_speed = 10

def update():
    if held_keys["escape"] == 1:
        app.userExit()

    

    #player.x += held_keys["d"] * velocity
    #player.x -= held_keys["a"] * velocity
    #player.y += held_keys["w"] * velocity
    #player.y -= held_keys["s"] * velocity
#
    #player.rotation_x += held_keys["r"] * 5
    #player.rotation_y += held_keys["r"] * 5

app.run()