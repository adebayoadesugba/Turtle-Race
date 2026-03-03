from turtle import Turtle, Screen
import turtle as t  
import random



is_racing = False

screen = Screen()
screen.setup(width=1000,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race").capitalize()
print(user_bet)

position = [-180, -100, 0, 100, 180]
randomMove = random.randint(1,10)
color_list = ["Blue", "Green", "Red", "Black", "Yellow", "SlateGray", "SeaGreen"]
screen.title("The Turtle Race")

all_turtle = []

for turtles in range(0,5):
    timmy = Turtle(shape="turtle")
    timmy.color(color_list[turtles])
    timmy.penup()
    timmy.goto(x=-480, y=position[turtles])
    all_turtle.append(timmy)

 

if user_bet:
    is_racing = True


while is_racing:
    for turtles in all_turtle:

        if turtles.xcor() > 480:
            is_racing = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"The {user_bet} Turtle won the race, so you BET was right and you win")
            else:
                print(f"The {winner} Turtle won the race, so you BET was wrong and you lose")
# Print the remaining turtles position
            for turtle in all_turtle:                print(f"{turtle.pencolor()} is at position {turtle.xcor()}")
        speed_o = random.randint(1,10)
        turtles.forward(speed_o)
        

    

if user_bet:
    pass






# print(randomMove)
# def move_forward():
#     timmy.forward(tim_random)
#     t_blue.forward(t_blueR)
#     t_green.forward(t_greenR)
#     t_yellow.forward(t_yellowR)
#     t_orange.forward(t_orangeR)

# def move_backward():
#     timmy.back(10)

# def turn_left():
#     timmy.left(10)

# def turn_right():
#     timmy.right(10)

# def clear_screen():
#     timmy.home()
#     timmy.clear()
    

screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear_screen)






















screen.exitonclick()