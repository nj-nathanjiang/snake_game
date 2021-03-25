import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def game_on_false():
    global game_is_on
    game_is_on = False


print("Make sure that you don't press two keys at once, or else you will lose.")
print("Press 'e' to exit.")
color = input("What color snake do you want? (red/orange/yellow/dark green/blue/purple) ").lower()
fruit_color = input("What fruit do you want your snake to eat? Please enter the color. "
                    "\n(apple: red/orange: orange/grape: dark magenta/blueberry: dark slate blue/watermelon: green) ")

screen = t.Screen()
screen.setup(1200, 850)

screen.bgcolor("black")
screen.title("Snake")

speed = 25
snake = Snake(color, speed)
food = Food(fruit_color)
scoreboard = Scoreboard()
screen.tracer(0)

snake.make_snake()
screen.listen()

game_is_on = True
while game_is_on:
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(game_on_false, "e")
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    if snake.squares[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    if snake.squares[0].xcor() > 600 or snake.squares[0].xcor() < -600 or snake.squares[0].ycor() > 425 or snake.squares[0].ycor() < -425:
        scoreboard.reset_game()
        snake.reset()

    for square in snake.squares[2:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset_game()
            snake.reset()


screen.exitonclick()
