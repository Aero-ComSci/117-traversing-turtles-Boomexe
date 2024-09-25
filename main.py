from custom_turtle import CustomTurtle
import turtle as trtl
import time

window = trtl.Screen()

turtles = []

for i, shape in enumerate(CustomTurtle.turtle_shapes):
    t = CustomTurtle(0, 0, shape, CustomTurtle.turtle_colors[i])
    turtles.append(t)

def draw_tree():
    start_x, start_y = 0, 0

    for turtle in turtles:
        turtle.set_start_position_without_moving(start_x, start_y)

        start_x += 50
        start_y += 50

    for turtle in turtles:
        turtle.draw_tree()
        print(turtle)

# NOTE: This is an extremely funny pun. Please laugh.
def draw_octa_nota_gon():
    start_x, start_y = 0, 0
    turtle_heading = 0

    for turtle in turtles:
        turtle.set_start_position_without_moving(start_x, start_y)
        turtle.draw_octagon(turtle_heading)

        start_x, start_y = turtle.get_turtle_pos()
        turtle_heading += 45

draw_tree()
time.sleep(2)

for turtle in turtles:
    turtle.clear()

draw_octa_nota_gon()

window.mainloop()