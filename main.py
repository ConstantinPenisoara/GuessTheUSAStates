import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

game_is_on = True
correct_answers = 0
inputted_state_list = []

while game_is_on:
    answer_state = screen.textinput(title=f"{correct_answers}/{len(data)} Guess the State",
                                    prompt="What's another state's name?").title()
    for state in data.state:
        if state == answer_state and answer_state not in inputted_state_list:
            new_answer = turtle.Turtle()
            new_answer.penup()
            new_answer.hideturtle()
            x_cor = int(data[data.state == answer_state].x)
            y_cor = int(data[data.state == answer_state].y)
            new_answer.goto(x_cor, y_cor)
            new_answer.write(answer_state)
            correct_answers += 1
            inputted_state_list.append(answer_state)
    if len(inputted_state_list) == len(data.state):
        game_is_on = False
    if answer_state == "Exit":
        states_to_learn = []
        for state in data.state:
            if state not in inputted_state_list:
                states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.cvs")
        break
