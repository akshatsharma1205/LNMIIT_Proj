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

a_cord = [-300, 200]
b_cord = [-150, 200]
c_cord = [0, 200]
d_cord = [150, 200]

def maca(sender, receiver):
  print("\nLets Begin...")

  #Defined all the turtles with a lil bit description
  draw1 = turtle.Turtle()
  draw2 = turtle.Turtle()
  draw3 = turtle.Turtle()
  draw1.speed(0)
  draw1.color("white")
  draw2.speed(0)
  draw2.color("white")
  draw3.speed(0)
  draw3.color("white")

  #Just checked who is the sender and got the co-ordinates & node properties.
  if sender in "A":
    final = a
    cord = a_cord
  elif sender in "B":
    final = b
    cord = b_cord
  elif sender in "C":
    final = c
    cord = c_cord
  else:
    final = d
    cord = d_cord

  time.sleep(3)

  #I'll hide all the turtle pointers.
  draw2.ht()
  draw1.ht()
  draw3.ht()

  if True:
    #All the turtles arrive on the Sender Node
    draw1.goto(cord)
    draw2.goto(cord)
    draw3.goto(cord)
  
    #Defined properties for the sender nodes.
    #I'm considering draw 3 for the initial RTS packet to the non-receiver node.
    #I'm considering draw 1 and draw 2 to lead the further RTS & CTS with the receiver node.
    draw3.color("violet")
    draw2.color("white")
    draw1.color("red")
    draw1.width(30)
    draw1.speed(1)
    draw3.width(30)

    #Now, let's send the RTS packet to the reciver and non-receiver node.

    #If the left or right is NONE, then draw3 should not act, thus making draw3 properties none
    #if final.left and final.right is None:
      #I'll set the draw 3 color the white so that it doesn't affect the code.
      
    
    #Here, I'll set the turtle face, where they have to proceed.
    # for that, we need to check if the receiver is in the left/right of the sender.
    # face = True means in right.
    if final.left is None:
      face = True
      draw3.color("white")
      draw3.width(1)
    elif final.right is None:
      face = False
      draw3.color("white")
      draw3.width(1)
    elif receiver in final.left:
      face = False
    else:
      face = True

    #Turning the faces of turtles.
    if face:
      draw2.left(315)
      draw1.left(315)
      draw3.left(225)
    else:
      draw2.left(225)
      draw1.left(225)
      draw3.left(315)

    # To get the animation effect : )
    print("Sender is sending the RTS (Request to Send) Packet ...")
    for _ in range(210):
      draw3.forward(1)
      draw1.forward(1)
      draw2.forward(1)


    draw2.color("red")
    time.sleep(2)

    draw2.width(30)
    draw2.speed(1)
    
    #checked
    if face:
      draw2.left(270)
    else:
      draw2.left(90)


    draw1.color("violet")
    print("Receiver is reverting with the CTS (Clear to Send) Packet ...")
    for _ in range(210):
      draw2.forward(1)
      draw1.forward(1)
    

    time.sleep(1)
    #Sending the Data Packet
    print("Sender is sending the DATA packet..")
    if face:
      draw2.left(90)
    else:
      draw2.left(270)

    draw2.color("green")
    
    draw2.width(60)
    draw2.forward(210)

    #Sending the Acknowledgement
    print("Receiver is sending Acknowledgement...")
    if face:
      draw2.left(225)
    else:
      draw2.left(135)

    draw2.width(10)
    draw2.forward(150)

    time.sleep(1)
    print("This program illustrates the MACA (Multiple Access Collision Avoidance) Protocol. \nThanks for your time.")





def __main__(sender, receiver):
  print("Input Received!")
  wn = turtle.Screen()
  wn.title("MACA Protocol")
  wn.bgcolor("white")
  wn.setup(width=800, height=600)
  #wn.tracer(0)


  # Node A
  node_a = turtle.Turtle()
  node_a.speed(0)
  node_a.shape("square")
  node_a.color("black")
  node_a.shapesize(stretch_wid=2,stretch_len=2)
  node_a.penup()
  node_a.goto(a_cord)

  line_a = turtle.Turtle()
  line_a.color("white")
  line_a.goto(a_cord)
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
  node_b.goto(b_cord)

  line_b = turtle.Turtle()
  line_b.color("white")
  line_b.goto(b_cord)
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
  node_c.goto(c_cord)

  line_c = turtle.Turtle()
  line_c.color("white")
  line_c.goto(c_cord)
  line_c.color("blue")
  line_c.left(270)
  line_c.forward(610)
  line_c.penup()

  pen.goto(0, 220)
  pen.write("C")

  # Node D 
  node_d = turtle.Turtle()
  node_d.speed(0)
  node_d.shape("square")
  node_d.color("green")
  node_d.shapesize(stretch_wid=2,stretch_len=2)
  node_d.penup()
  node_d.goto(d_cord)

  line_d = turtle.Turtle()
  line_d.color("white")
  line_d.goto(d_cord)
  line_d.color("green")
  line_d.left(270)
  line_d.forward(610)
  line_d.penup()

  pen.goto(150, 220)
  pen.write("D")

  print("\nThe sender is:" + sender)
  print("The receiver is:" + receiver)
  maca(sender, receiver)
  