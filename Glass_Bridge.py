import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina(vsync=True)
Sky(texture = "sky_sunset")
window_title = "Glass Bridge"
ahmedgames = Text(text="ahmedgames presents",color=color.gray,x=-0.2,y=0.3)
glass = Text(text="Glass",scale=(5,5),color=color.gray,x=-0.2,y=0.2)
crossing = Text(text="Bridge",scale=(5,5),color=color.gray,x=-0.2,y=0)
press = Text(text="press Enter to begin",color=color.gray,x=-0.2,y=-0.3)
close = Text(text="press any button to close",color=color.gray,x=-0.2,y=-0.4)
camera.y = 15
#player
#player = FirstPersonController()
you_lose = Text(text = "You Fell",x=100,y=100,scale=(5,5),color = color.red)
restart = Text(text = "press L to restart",x=100,y=100,scale=(3,3),color = color.red)


#Random
level1 = random.randint(1,2)
if level1 == 1:
    choice1 = "mesh"
else:
    choice1 = "none"

level2 = random.randint(1,2)
if level2 == 2:
    choice2 = "mesh"
else:
    choice2 = "none"

level3 = random.randint(1,2)
if level3 == 1:
    choice3 = "mesh"
else:
    choice3 = "none"

level4 = random.randint(1,2)
if level4 == 2:
    choice4 = "mesh"
else:
    choice4 = "none"


if choice1 == choice2:
    choice2 = "mesh"
    choice1 = "none"
if choice3 == choice4:
    choice3 = "mesh"
    choice4 = "none"



#menu_floor
spawn_floor = Entity(model="cube",scale=(15,0,80),postion=(22,1,25),color = color.white66,collider="mesh")

#Level1
floor2 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,45),rotation=(0,90,0),color = color.white10,collider=f"{choice1}")

floor3 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,45),rotation=(0,90,0),color = color.white33,collider=f"{choice2}")

floor4 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,60),rotation=(0,90,0),color = color.white50,collider=f"{choice3}")

floor5 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,60),rotation=(0,90,0),color = color.white66,collider=f"{choice4}")

floor6 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,75),rotation=(0,90,0),color = color.white10,collider=f"{choice1}")

floor7 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,75),rotation=(0,90,0),color = color.white33,collider=f"{choice2}")

floor8 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,90),rotation=(0,90,0),color = color.white50,collider=f"{choice3}")

floor9 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,90),rotation=(0,90,0),color = color.white66,collider=f"{choice4}")

floor11 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,105),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")

floor12 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,105),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")

floor13 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,120),rotation=(0,90,0),color = color.white66,collider=f"{choice3}")

floor14 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,120),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")

floor15 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,135),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")

floor16 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,135),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")

floor17 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,150),rotation=(0,90,0),color = color.white66,collider=f"{choice3}")

floor18 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,150),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")

floor19 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,165),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")

floor20 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,165),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")

floor21 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,180),rotation=(0,90,0),color = color.white66,collider=f"{choice3}")

floor22 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,180),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")

floor23 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,195),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")

floor24 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,195),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")

floor25 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,210),rotation=(0,90,0),color = color.white66,collider=f"{choice3}")

floor26 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,210),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")

floor27 = Entity(model="cube",scale=(15,0,8),position=(-2,0.5,225),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")

floor28 = Entity(model="cube",scale=(15,0,8),position=(6,0.5,225),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")


#Level 2
floor2_1 = Entity(model="cube",scale=(15,0,8),position=(-2,20,45),rotation=(0,90,0),color = color.white66,collider=f"mesh")
floor2_2 = Entity(model="cube",scale=(15,0,8),position=(6,20,45),rotation=(0,90,0),color=color.white10,collider=f"mesh")
floor2_3 = Entity(model="cube",scale=(15,0,8),position=(6,20,60),rotation=(0,90,0),color=color.white33,collider=f"{choice1}")
floor2_4 = Entity(model="cube",scale=(15,0,8),position=(-2,20,60),rotation=(0,90,0),color=color.white50,collider=f"{choice2}")
floor2_5 = Entity(model="cube",scale=(15,0,8),position=(-2,20,75),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor2_6 = Entity(model="cube",scale=(15,0,8),position=(6,20,75),rotation=(0,90,0),color=color.white10,collider=f"{choice4}")
floor2_7 = Entity(model="cube",scale=(15,0,8),position=(-2,20,90),rotation=(0,90,0),color=color.white33,collider=f"{choice1}")
floor2_8 = Entity(model="cube",scale=(15,0,8),position=(6,20,90),rotation=(0,90,0),color=color.white50,collider=f"{choice2}")
floor2_9 = Entity(model="cube",scale=(15,0,8),position=(-2,20,105),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor2_10 = Entity(model="cube",scale=(15,0,8),position=(6,20,105),rotation=(0,90,0),color=color.white10,collider=f"{choice4}")
floor2_11 = Entity(model="cube",scale=(15,0,8),position=(-2,20,120),rotation=(0,90,0),color=color.white33,collider=f"{choice1}")
floor2_12 = Entity(model="cube",scale=(15,0,8),position=(6,20,120),rotation=(0,90,0),color=color.white50,collider=f"{choice2}")
floor2_13 = Entity(model="cube",scale=(15,0,8),position=(-2,20,135),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor2_14 = Entity(model="cube",scale=(15,0,8),position=(6,20,135),rotation=(0,90,0),color=color.white10,collider=f"{choice4}")
floor2_15 = Entity(model="cube",scale=(15,0,8),position=(-2,20,150),rotation=(0,90,0),color=color.white50,collider=f"{choice1}")
floor2_16 = Entity(model="cube",scale=(15,0,8),position=(6,20,150),rotation=(0,90,0),color=color.white33,collider=f"{choice2}")
floor2_18 = Entity(model="cube",scale=(15,0,8),position=(6,20,165),rotation=(0,90,0),color=color.white10,collider=f"{choice3}")
floor2_19 = Entity(model="cube",scale=(15,0,8),position=(-2,20,165),rotation=(0,90,0),color=color.white50,collider=f"{choice4}")
floor2_20 = Entity(model="cube",scale=(15,0,8),position=(-2,20,180),rotation=(0,90,0),color=color.white33,collider=f"{choice1}")
floor2_20 = Entity(model="cube",scale=(15,0,8),position=(6,20,180),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")
floor2_21 = Entity(model="cube",scale=(15,0,8),position=(6,20,195),rotation=(0,90,0),color = color.white10,collider=f"{choice3}")
floor2_22 = Entity(model="cube",scale=(15,0,8),position=(-2,20,195),rotation=(0,90,0),color = color.white66,collider=f"{choice4}")
floor2_23 = Entity(model="cube",scale=(15,0,8),position=(-2,20,210),rotation=(0,90,0),color = color.white33,collider=f"{choice1}")
floor2_24 = Entity(model="cube",scale=(15,0,8),position=(6,20,210),rotation=(0,90,0),color = color.white50,collider=f"{choice2}")
floor2_24 = Entity(model="cube",scale=(15,0,8),position=(6,20,225),rotation=(0,90,0),color = color.white10,collider=f"{choice3}")
floor2_25 = Entity(model="cube",scale=(15,0,8),position=(-2,20,225),rotation=(0,90,0),color = color.white66,collider=f"{choice4}")




#Level3
floor3_1 = Entity(model="cube",scale=(15,0,8),position=(-2,40,45),rotation=(0,90,0),color = color.white10,collider=f"mesh")
floor3_2 = Entity(model="cube",scale=(15,0,8),position=(6,40,45),rotation=(0,90,0),color=color.white50,collider=f"mesh")
floor3_3 = Entity(model="cube",scale=(15,0,8),position=(6,40,60),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor3_4 = Entity(model="cube",scale=(15,0,8),position=(-2,40,60),rotation=(0,90,0),color=color.white33,collider=f"{choice4}")
floor3_5 = Entity(model="cube",scale=(15,0,8),position=(-2,40,75),rotation=(0,90,0),color=color.white66,collider=f"{choice1}")
floor3_6 = Entity(model="cube",scale=(15,0,8),position=(6,40,75),rotation=(0,90,0),color=color.white10,collider=f"{choice2}")
floor3_7 = Entity(model="cube",scale=(15,0,8),position=(-2,40,90),rotation=(0,90,0),color=color.white50,collider=f"{choice3}")
floor3_8 = Entity(model="cube",scale=(15,0,8),position=(6,40,90),rotation=(0,90,0),color=color.white10,collider=f"{choice4}")
floor3_9 = Entity(model="cube",scale=(15,0,8),position=(-2,40,105),rotation=(0,90,0),color=color.white66,collider=f"{choice1}")
floor3_10 = Entity(model="cube",scale=(15,0,8),position=(6,40,105),rotation=(0,90,0),color=color.white50,collider=f"{choice2}")
floor3_11 = Entity(model="cube",scale=(15,0,8),position=(-2,40,120),rotation=(0,90,0),color=color.white10,collider=f"{choice3}")
floor3_12 = Entity(model="cube",scale=(15,0,8),position=(6,40,120),rotation=(0,90,0),color=color.white33,collider=f"{choice4}")
floor3_13 = Entity(model="cube",scale=(15,0,8),position=(-2,40,135),rotation=(0,90,0),color=color.white50,collider=f"{choice1}")
floor3_14 = Entity(model="cube",scale=(15,0,8),position=(6,40,135),rotation=(0,90,0),color=color.white10,collider=f"{choice2}")
floor3_15 = Entity(model="cube",scale=(15,0,8),position=(-2,40,150),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor3_16 = Entity(model="cube",scale=(15,0,8),position=(6,40,150),rotation=(0,90,0),color=color.white33,collider=f"{choice4}")
floor3_18 = Entity(model="cube",scale=(15,0,8),position=(6,40,165),rotation=(0,90,0),color=color.white10,collider=f"{choice1}")
floor3_19 = Entity(model="cube",scale=(15,0,8),position=(-2,40,165),rotation=(0,90,0),color=color.white33,collider=f"{choice2}")
floor3_20 = Entity(model="cube",scale=(15,0,8),position=(-2,40,180),rotation=(0,90,0),color=color.white66,collider=f"{choice3}")
floor3_20 = Entity(model="cube",scale=(15,0,8),position=(6,40,180),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")
floor3_21 = Entity(model="cube",scale=(15,0,8),position=(6,40,195),rotation=(0,90,0),color = color.white10,collider=f"{choice1}")
floor3_22 = Entity(model="cube",scale=(15,0,8),position=(-2,40,195),rotation=(0,90,0),color = color.white33,collider=f"{choice2}")
floor3_23 = Entity(model="cube",scale=(15,0,8),position=(-2,40,210),rotation=(0,90,0),color = color.white50,collider=f"{choice3}")
floor3_24 = Entity(model="cube",scale=(15,0,8),position=(6,40,210),rotation=(0,90,0),color = color.white10,collider=f"{choice4}")
floor3_24 = Entity(model="cube",scale=(15,0,8),position=(6,40,225),rotation=(0,90,0),color = color.white66,collider=f"{choice1}")
floor3_25 = Entity(model="cube",scale=(15,0,8),position=(-2,40,225),rotation=(0,90,0),color = color.white10,collider=f"{choice2}")


def input(key):
    if key == "enter":
        global player
        player = FirstPersonController()
        global level1
        level1 = Text(text= "Level 1",x=0.5,y=0.5,scale=(3,3),color = color.dark_gray)
        ahmedgames.y = 100
        glass.y = 100
        crossing.y = 100
        press.y = 100
        close.y = 100
        place = Text(text="Press Q to quit",x=-0.8,y=0.5,scale=(2,2),color = color.dark_gray)
    if player.y < -1:
        you_lose.x = -0.4
        you_lose.y = 0.3
        restart.x = 0
        restart.y = 0.2
        if key == "l":
            player.y = 1
            player.z = 31
            temp_lose = False
            you_lose.y = 100
            restart.y = 100
    if player.z > 220 and player.y < 20:
                player.z = 40
                player.y = 21
                level1.y = 200
                global level2
                level2 = Text(text="Level 2",x=0.5,y=0.5,scale=(3,3),color = color.dark_gray)
    if player.z > 220 and player.y > 20 and player.y < 40 :
        player.z = 40
        player.y = 41
        level2.y = 80
        global level3
        level3 = Text(text="level 3",x=0.5,y=0.5,scale=(3,3),color = color.dark_gray)
    if player.z > 220 and player.y > 40:
        You_WIN = Text(text="You WIN",x=-0.3,y=0.5,scale=(5,5),color = color.green)
        Glass_Bridge = Text(text="Glass Bridge",x=-0.3,y=0.3,scale=(3,3),color = color.gray)
        programmer = Text(text="Technical Programmer:Hamza Ahmed",x=-0.3,y=0.1,scale=(2,2),color = color.gray)
        Thank = Text(text="Thank",x=-0.1,y=0,scale=(5,5),color = color.red)
        you = Text(text="You",x=0,y=-0.1,scale=(5,5),color = color.red)


    if key == "q":
        application.quit()


app.run()
