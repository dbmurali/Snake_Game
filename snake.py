from turtle import Turtle


LEFT=180
RIGHT=0
DOWN=270
UP=90
class Snake:

    def __init__(self):

        self.snake_tail = []
        self.create()
        self.head=self.snake_tail[0]


    def create(self):
        # CREATING SNAKE SEGMENTS
        start_positions = [(0, 0), (-20, 0), (-40, 0),(-60,0),(-80,0),(-100,0),(-120,0),(-140,0),(-160,0),(-180,0),(-200,0),(-210,0),(-220,0),]
        for position in start_positions:
           self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle("square")
        segment.fillcolor("white")
        segment.penup()
        segment.goto(position)
        self.snake_tail.append(segment)



    # MOVE METHOD
    def move(self):
        """METHOD USED TO LINKING THE SNAKE SEGMENTS AND MADE TO FOLLOW EACH """
        for i in range(len(self.snake_tail)-1,0,-1):
            x=self.snake_tail[i-1].xcor()
            y=self.snake_tail[i-1].ycor()
            self.snake_tail[i].goto(x=x,y=y)
        self.snake_tail[0].fd(20)

    def extend(self):
        last_segment=self.snake_tail[-1]
        position=(last_segment.xcor(),last_segment.ycor())
        self.add_segment(position)



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

