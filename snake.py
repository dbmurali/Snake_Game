from turtle import Turtle

LEFT=180
RIGHT=0
DOWN=270
UP=90
class Snake:

    def __init__(self):
        self.snake_tail = []
        self.snake_length=3
        segment_pos=0

        # CREATING SNAKE SEGMENTS
        for segments in range(self.snake_length):
            segment=Turtle("square")
            segment.fillcolor("white")
            segment.penup()
            segment.goto(x=segment_pos,y=0)
            self.snake_tail.append(segment)
            segment_pos-=20
        self.head = self.snake_tail[0]


    # MOVE METHOD
    def move(self):
        """METHOD USED TO LINKING THE SNAKE SEGMENTS AND MADE TO FOLLOW EACH """
        for i in range(len(self.snake_tail)-1,0,-1):
            x=self.snake_tail[i-1].xcor()
            y=self.snake_tail[i-1].ycor()
            self.snake_tail[i].goto(x=x,y=y)
        self.snake_tail[0].fd(20)




    #KEY CONTROL
    def up(self):
        if self.head.heading() !=DOWN:
          self.snake_tail[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_tail[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_tail[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
         self.snake_tail[0].setheading(LEFT)

