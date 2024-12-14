import turtle

turtle.bgcolor("skyblue")
turtle.speed(1500)

#The table funtion
def table(x,y,width,height,ang, fill_color):

    #First Layer of the table
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(width)
    turtle.left(ang)
    turtle.forward(height)
    turtle.left(ang)
    turtle.forward(width)
    turtle.left(ang)
    turtle.forward(height)
    turtle.left(ang)
    turtle.end_fill()
    

    
    turtle.penup()
    turtle.goto(x, y)  
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(width)
    turtle.right(ang)
    turtle.forward(height)
    turtle.right(ang)
    turtle.forward(width)
    turtle.right(ang)
    turtle.forward(height)
    turtle.right(ang)
    turtle.end_fill()

def first_layer(x, y, fill_color, side, ang, side2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.end_fill()
    turtle.penup()

def second_layer(x, y, fill_color, side, ang, side2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.end_fill()
    turtle.penup()

def third_layer(x, y, fill_color, side, ang, side2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.end_fill()
    turtle.penup()

def fourth_layer(x, y, fill_color, side, ang, side2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.end_fill()
    turtle.penup()

#The frosting cream funtion
def frosting(x,y,fill_color, side,ang,ang2,r):
    turtle.speed(4)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.right(ang)
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(r,ang2)
    turtle.right(ang)
    turtle.forward(side)
    turtle.right(ang)
    turtle.circle(r,ang2)
    turtle.right(ang)
    turtle.forward(side)
    turtle.right(ang)
    turtle.circle(r,ang2)
    turtle.right(ang)
    turtle.forward(side)
    turtle.right(ang)
    turtle.circle(r,ang2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.right(ang)
    turtle.end_fill()

#The Cherry Circle function
def circle(x,y,fill_color,r):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.circle(r)
    turtle.end_fill()

# The Candle Function
def candle(x, y, side, side2,ang, fill_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.right(ang)
    turtle.forward(side2)
    turtle.right(ang)
    turtle.forward(side)
    turtle.right(ang)
    turtle.forward(side2)
    turtle.right(ang)
    
    turtle.end_fill()

#The Flame Function
def flame(x, y, side,side2,ang, fill_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(fill_color)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.forward(side)
    turtle.left(ang)
    turtle.forward(side2)
    turtle.left(ang)
    turtle.end_fill()

#The Table 
table(-150, -165, 320, 10, 90, "saddle brown")
table(-150,-225,20,50,90,"saddle brown")
table(150,-225,20,50,90,"saddle brown")
table(-100,-225,20,50,90,"saddle brown")
table(100,-225,20,50,90,"saddle brown")

#Cake Layers
first_layer(-100, -153, "pink", 200, 90, 30)
second_layer(-100, -123, "red", 200, 90, 30)
third_layer(-100, -92, "orange", 200, 90, 50)
fourth_layer(-100, -42, "yellow", 200, 90, 50)

#The Cherry Circle 
circle(5,7,"red",15)

#The frosting Cream 
frosting(-100,8,"white",1,90,180,25)

#Candle & Flame
candle(-20, 10, 30, -10,90, "royal blue")  
flame(-30, 41,10,-10,90, "orange")  

input("")