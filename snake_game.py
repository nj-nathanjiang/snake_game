import turtle as t
import time
from snake import Snake

color = input("What color snake do you want? (red/orange/yellow/dark green/blue/purple) ").lower()

size = input("How large do you want the map to be? (small/medium/large) ").lower()

speed = input("How fast do you want your snake to be? (fast/medium/slow) ").lower()
if speed == "fast":
    speed = 25
elif speed == "medium":
    speed = 20
else:
    speed = 15

screen = t.Screen()
if size == "medium":
    screen.setup(width=600, height=600)
elif size == "large":
    screen.setup(width=800, height=800)
else:
    screen.setup(width=400, height=400)

screen.bgcolor("black")
screen.title("Snake")

snake = Snake(color, speed)
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


screen.exitonclick()
