from turtle import Turtle
class Ball(Turtle):
	def __init__(self,r,color,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.r = r
		self.dx = dx
		self.dy = dy
		self.shape("Circle")
		self.color(color)
		self.turtlesize(r/10)

	def move(self,screen_width,screen_height):
		current_x = self.xpos()
		new_x = current_x + dx
		current_y = self.ypos()
		new_y = current_y + dy
		right_side_ball = new_x + r
		left_side_ball = new_x - r
		top_side_ball= new_y + r
		bottom_side_ball = new_y - r
		self.goto(new_x, new_y)
		if left_side_ball > -screen_width:
			self.goto(screen_width)
