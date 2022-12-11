import turtle
import pandas


def get_coor_mouse_click(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("States Game")
screen.setup(750, 800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

country = pandas.read_csv("50_states.csv")
states = country.state
all_states = states.to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    user_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's "
                                                                                             "name? ").capitalize()

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if user_answer in all_states and user_answer not in correct_guesses:
        correct_guesses.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = country[states == user_answer]
        state_coor = (int(state_data.x), int(state_data.y))
        t.goto(state_coor)
        t.write(user_answer)

# turtle.mainloop()
# screen.exitonclick()
