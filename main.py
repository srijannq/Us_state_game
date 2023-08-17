import turtle
import pandas

data = pandas.read_csv("50_states.csv")

data_country = data["state"]

data_country_list = data_country.to_list()
print(data_country_list)
screen = turtle.Screen()

screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
t1 = turtle.Turtle("blank_states_img.gif")
t2 = turtle.Turtle()
t2.ht()
t2.penup()
answer_list = []
flag = True
while flag:
    answer_state = screen.textinput(title=f"{len(answer_list)}/{len(data_country_list)}  states correct",
                                    prompt="What is the name of the "
                                           "state")
    answer_state_title = answer_state.title()
    if answer_state_title in data_country_list:
        if answer_state_title not in answer_list:
            state_data = data[data.state == answer_state_title]
            answer_list.append(answer_state)

            t2.goto(int(state_data.x), int(state_data.y))

            t2.write(f"{answer_state}", move=False, font=('Arial', 10, 'normal'))
    if len(answer_list) == 50:
        flag = False

screen.exitonclick()
