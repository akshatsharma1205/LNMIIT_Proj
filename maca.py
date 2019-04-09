import turtle
import time


class Node:
  """the left and right of a node represent it's neighbour & state represents the availability"""
  def __init__(self, left, right):
    self.left = left
    self.right = right
    self.state = True
    
a = Node(None, "B")
b = Node("A", "C")
c = Node("B", "D")
d = Node("C", None)

def __main__(sender, receiver):
  wn = turtle.Screen()
  wn.title("MACA Protocol")
  wn.bgcolor("white")
  wn.setup(width=800, height=600)
  wn.tracer(0)

  a_cord = [-300, 200]
  b_cord = [-150, 200]
  c_cord = [125, 200]
  d_cord = [300, 200]

  # Node A
  node_a = turtle.Turtle()
  node_a.speed(0)
  node_a.shape("square")
  node_a.color("black")
  node_a.shapesize(stretch_wid=2,stretch_len=2)
  node_a.penup()
  node_a.goto(-300, 200)

  line_a = turtle.Turtle()
  line_a.color("white")
  line_a.goto(-300, 200)
  line_a.color("black")
  line_a.left(270)
  line_a.forward(610)
  line_a.penup()

  pen = turtle.Turtle()
  pen.speed(0)
  pen.shape("square")
  pen.color("black")
  pen.penup()
  pen.hideturtle()
  pen.goto(-300, 220)
  pen.write("A")

  # Node B
  node_b = turtle.Turtle()
  node_b.speed(0)
  node_b.shape("square")
  node_b.color("red")
  node_b.shapesize(stretch_wid=2,stretch_len=2)
  node_b.penup()
  node_b.goto(-150, 200)

  line_b = turtle.Turtle()
  line_b.color("white")
  line_b.goto(-150, 200)
  line_b.color("red")
  line_b.left(270)
  line_b.forward(610)
  line_b.penup()

  pen.goto(-150, 220)
  pen.write("B")

  # Node C
  node_c = turtle.Turtle()
  node_c.speed(0)
  node_c.shape("square")
  node_c.color("blue")
  node_c.shapesize(stretch_wid=2,stretch_len=2)
  node_c.penup()
  node_c.goto(125, 200)

  line_c = turtle.Turtle()
  line_c.color("white")
  line_c.goto(125, 200)
  line_c.color("blue")
  line_c.left(270)
  line_c.forward(610)
  line_c.penup()

  pen.goto(125, 220)
  pen.write("C")

  # Node D 
  node_d = turtle.Turtle()
  node_d.speed(0)
  node_d.shape("square")
  node_d.color("green")
  node_d.shapesize(stretch_wid=2,stretch_len=2)
  node_d.penup()
  node_d.goto(300, 200)

  line_d = turtle.Turtle()
  line_d.color("white")
  line_d.goto(300, 200)
  line_d.color("green")
  line_d.left(270)
  line_d.forward(610)
  line_d.penup()

  pen.goto(300, 220)
  pen.write("D")

  while True:
    wn.update()

    #time.sleep(10)
    print("The sender is:" + sender)
    print("\nThe receiver is:" + receiver)

    #time.sleep(3)
    draw1 = turtle.Turtle()
    draw1.speed(1)
    draw1.color("white")

    if sender is "A":
      draw1.goto(a_cord)
    elif sender is "B":
      draw1.goto(b_cord)
    elif sender is "C":
      draw1.goto(c_cord)
    else:
      draw1.goto(d_cord)

    draw1.width(50)
    draw1.forward(100)





# #Main Loop
# while True:
#   wn.update()