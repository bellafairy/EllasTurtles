import turtle
screen = turtle.Screen()
screen.bgcolor('maroon')

bania_turtles = dict()
bania_names = ['danelle', 'oliver', 'addy', 'patton', 'buck']
bania_fg_colors = ['black', 'black', 'black', 'black', 'black']
bania_bg_colors = ['red', 'orange', 'yellow', 'green', 'blue']

for name in bania_names:
    t = turtle.Turtle()
    t.shape('turtle')
    t.penup()
    bania_turtles[name] = t


for index, name in enumerate(bania_names):
    bania_turtles[name].color(
        bania_fg_colors[index],
        bania_bg_colors[index])
for y in {0, -100}:
    for x in {0, -100}:
        print([x, y])
bania_turtles['buck'].setposition(-50, 100)
bania_turtles['patton'].setposition(0, 0)
bania_turtles['addy'].setposition(-100, 0)
bania_turtles['oliver'].setposition(0, -100)
bania_turtles['danelle'].setposition(-100, -100)

for t in bania_turtles.values():
    t.pendown()
    t.begin_fill()
    # triangles
    for number in range(3):
        t.forward(120)
        t.left(120)
    t.end_fill()
screen.exitonclick()
screen.mainloop()