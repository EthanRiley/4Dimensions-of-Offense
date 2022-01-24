import turtle

def drawdimensions(ortgrank, pacerank,moreyrank, ballrank, playerrank):
    pace_dimension = (31-pacerank)*8
    morey_dimension = (31 - moreyrank)*8
    player_dimension = (31-playerrank)*8
    ball_dimension = (31-playerrank)*8
    turtle.hideturtle()
    turtle.setposition(0,0)
    turtle.penup()
    turtle.forward(pace_dimension)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(ball_dimension)
    turtle.left(90)
    turtle.forward(player_dimension+pace_dimension)
    turtle.left(90)
    turtle.forward(ball_dimension+morey_dimension)
    turtle.left(90)
    turtle.forward(player_dimension+pace_dimension)
    turtle.left(90)
    turtle.forward(morey_dimension+ball_dimension)


drawdimensions(115, 10, 9, 30, 28)

t = turtle.Turtle()
t.hideturtle()
t.pencolor("blue")
t.setposition(0,0)
t.forward(250)
t.setposition(0,0)
t.right(90)
t.forward(250)
t.setposition(0,0)
t.backward(250)
t.setposition(0,0)
t.left(90)
t.backward(250)



def main():

    main()

