"""snake class"""
from turtle import Turtle

BEGIN_X_COR = 0
BEGIN_Y_COR = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """snake class"""

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        """initialize the snake body"""
        for i in range(3):
            snake_block = Turtle("square")
            snake_block.color("white")
            snake_block.penup()
            x = BEGIN_X_COR - i * 20
            y = BEGIN_Y_COR
            snake_block.goto(x, y)
            self.snake.append(snake_block)

        # Screen().update()

    def move(self):
        """snake move forward"""
        for block_num in range(len(self.snake) - 1, 0, -1):
            x = self.snake[block_num - 1].xcor()
            y = self.snake[block_num - 1].ycor()
            self.snake[block_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        """change the snake direction up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        """change the snake direction down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        """change the snake direction left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        """change the snake direction right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def __len__(self):
        """return the length of the snake"""
        return len(self.snake)
