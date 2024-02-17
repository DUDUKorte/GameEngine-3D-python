import csv
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.editor.level_editor import LevelEditor, LevelEditorScene

app = Ursina()
#editor = LevelEditor()
#my_scene = LevelEditorScene(0, 0, 'scene_01')
#my_scene.path = './scenes/'

#editor.disable()

# Create sky atmosphere and fog density
s = Sky()
scene.fog_density = .03 # exponential fog density
#scene.fog_density = (50, 200) # linear density fog


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
        self.fall_after = 0 #cannot jump

    def input(self, key):
        if key == "left shift":
            self.speed = lerp(self.speed, 10, 1)
        elif key == "left shift up":
            self.speed = 5

TextureBox()

player = myPlayer()

def input(key):
    global editor_mode

    if key == 'l':
        print('load scene')
        my_scene.load()
    elif key == 'k':
        print('saving scene')
        my_scene.save()


def update():
    if held_keys["escape"] == 1:
        app.userExit()

def load_scene_00():
    with open('scenes/untitled_scene[0,0].csv', newline='') as f:
        spamreader = csv.reader(f, delimiter=';', quotechar=' ')
        first = True
        for row in spamreader:
            if first:
                first = False
                continue
            if row:
                spawn_entity = Entity(position=row[1], model=row[2], shader=row[3], texture=row[4], collider=row[5], collider_type=row[6])

        # class;position;model;shader;texture;collider;collider_type
        # WhiteCube;Vec3(0.73366, 0.583259, -7.32422e-05);'cube';'lit_with_shadows_shader';'white_cube';'box';'None'
        #print(f'{scene}\n {type(scene)}'*80)

    # Load
    

app.run()