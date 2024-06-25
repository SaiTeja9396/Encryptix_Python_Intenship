import random
from tkinter import *
schema = {
    "Rock": {"Rock": 0, "Paper": 1, "Scissor": 2},
    "Paper": {"Rock": 2, "Paper": 0, "Scissor": 1},
    "Scissor": {"Rock": 1, "Paper": 2, "Scissor": 0}
}

comp_score = 0
play_score = 0

def outcome_handler(user_choice):
    global comp_score
    global play_score
    outcomes = ["Rock", "Paper", "Scissor"]
    random_number = random.randint(0, 2)
    computer_choice = outcomes[random_number]
    
    result = schema[user_choice][computer_choice]
    
    player_choice.config(fg="green", text="Player Choice : " + user_choice)
    computer_choice_label.config(fg="red", text="  Computer Choice : " + computer_choice)
    
    if result == 2:
        play_score += 2
        player_score.config(text="Player Score : " + str(play_score))
        outcome_label.config(fg="blue", text="  Outcome : Player Won ")
    elif result == 1:
        play_score += 1
        comp_score += 1
        player_score.config(text="Player Score : " + str(play_score))
        computer_score.config(text="Computer Score : " + str(comp_score))
        outcome_label.config(fg="blue", text="  Outcome : Draw ")
    elif result == 0:
        comp_score += 2
        computer_score.config(text="Computer Score : " + str(comp_score))
        outcome_label.config(fg="blue", text="  Outcome : Computer Won ")

root = Tk()
root.title("Rock Paper Scissors Game")

Label(root, text="Rock, Paper, Scissors", font="Arial").grid(row=0, columnspan=3, pady=10)
Label(root, text="Please select an option", font="Arial").grid(row=1, columnspan=3)

player_score = Label(root, text="Player Score : 0", font="Arial")
player_score.grid(row=2, column=0, sticky=W)

computer_score = Label(root, text="Computer Score : 0", font="Arial")
computer_score.grid(row=2, column=2, sticky=E)

player_choice = Label(root, font="Arial")
player_choice.grid(row=3, column=0)

computer_choice_label = Label(root, font="Arial")
computer_choice_label.grid(row=3, column=2)

outcome_label = Label(root, font="Arial")
outcome_label.grid(row=3, column=1)
Label(root).grid(row=5)

Button(root, text="Rock", width=15, command=lambda: outcome_handler("Rock")).grid(row=4, column=0, sticky=W, padx=5, pady=5)
Button(root, text="Paper", width=15, command=lambda: outcome_handler("Paper")).grid(row=4, column=1, sticky=N, padx=5, pady=5)
Button(root, text="Scissor", width=15, command=lambda: outcome_handler("Scissor")).grid(row=4, column=2, sticky=E, padx=5, pady=5)

root.mainloop()
