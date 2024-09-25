import turtle as trtl

class CustomTurtle:
    turtle_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
    turtle_colors = ['red', 'blue', 'green', 'orange', 'purple', 'gold']

    def __init__(self, x, y, turtle_shape, turtle_color) -> None:
        self.x = x
        self.y = y
        self.turtle_shape = turtle_shape
        self.turtle_color = turtle_color
        self.turtle = trtl.Turtle(shape=turtle_shape)
        self.turtle.color(turtle_color)
        # self.turtle.penup()
    
    def draw_tree(self):
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.right(45)
        self.turtle.forward(50)
        self.turtle.penup()

    def set_start_position_without_moving(self, new_x, new_y):
        self.x, self.y = new_x, new_y
    
    def get_turtle_pos(self):
        return self.turtle.pos()

    def goto(self, new_x, new_y):
        self.turtle.penup()
        self.turtle.goto(new_x, new_y)
        self.turtle.pendown()
    
    def clear(self):
        self.turtle.clear()

    def draw_octagon(self, heading):
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.pendown()
        self.turtle.setheading(heading)
        self.turtle.forward(100)
    
    def __str__(self):
        return f'Turtle Shape: {self.turtle_shape} | Turtle Color: {self.turtle_color}'