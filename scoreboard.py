import turtle as t
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("data.txt", "r") as file:
    high_score = int(file.read())


class Scoreboard(t.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 395)
        self.color("white")
        self.high_score = high_score
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", "w") as data_file:
            data_file.write(str(self.high_score))
