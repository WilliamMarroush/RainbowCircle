import arcade as arc, random
arc.open_window(800,666,'Pac-man')
#colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
cyan=(0,255,255)
light_dark_purple=(150,30,200)
dark_purple=(100,50,150)
random_color=(123,220,130)
purple = (189,55,180)
color_list=(white,red,green,blue,yellow,cyan,dark_purple,random_color,purple)
#Set Back
arc.set_background_color(black)
arc.start_render()
#=============================Drawing Begins==============================#
center=random.choice(color_list)
arc.draw_circle_filled(400,333,5,center)
radius=10
thick=7
for x in range(14):
    color=random.choice(color_list)
    arc.draw_circle_outline(400,333,radius,color,thick)
    radius+=10
    thick-=0.5
center=random.choice(color_list)
arc.draw_circle_filled(620,333,5,center)
radius=10
thick=7
for x in range(14):
    color=random.choice(color_list)
    arc.draw_circle_outline(620,333,radius,color,thick)
    radius+=10
    thick-=0.5
center=random.choice(color_list)
arc.draw_circle_filled(180,333,5,center)
radius=10
thick=7
for x in range(14):
    color=random.choice(color_list)
    arc.draw_circle_outline(180,333,radius,color,thick)
    radius+=10
    thick-=0.5
center=random.choice(color_list)
arc.draw_circle_filled(400,111,5,center)
radius=10
thick=7
for x in range(14):
    color=random.choice(color_list)
    arc.draw_circle_outline(400,111,radius,color,thick)
    radius+=10
    thick-=0.5
center=random.choice(color_list)
arc.draw_circle_filled(400,555,5,center)
radius=10
thick=7
for x in range(14):
    color=random.choice(color_list)
    arc.draw_circle_outline(400,555,radius,color,thick)
    radius+=10
    thick-=0.5
#=============================Drawing Ends================================#
arc.finish_render()
arc.run()

