import turtle as t

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self, color, speed):
        self.squares = []
        self.color = color
        self.speed = speed
        for position in POSITIONS:
            square_segment = t.Turtle(shape="square")
            square_segment.penup()
            square_segment.color(self.color)
            square_segment.goto(position)
            square_segment.showturtle()
            self.squares.append(square_segment)
        self.head = self.squares[0]

    def move_snake(self):
        for num in range(len(self.squares) - 1, 0, -1):
            xcor = self.squares[num - 1].xcor()
            ycor = self.squares[num - 1].ycor()
            self.squares[num].goto(xcor, ycor)
        self.squares[0].forward(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

