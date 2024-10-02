from tkinter import*
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [("rock",0), ("paper",1),("scissors",2)]

def computer_wins():
    global player_score, computer_score
    computer_score += 1
    winner_label.config(text="Computet Won!!")
    computer_score_label.config(text="Computer Score: "+str(computer_score))
    player_score_label.config(text="Player Score: "+str(player_score))

def player_wins():
    global player_score, computer_score
    player_score += 1
    winner_label.config(text="Player Won!!")
    player_score_label.config(text="Player Score: "+str(player_score))
    computer_score_label.config(text="Computer Score: "+str(computer_score))

def tie():
    global player_score, computer_score
    winner_label.config(text="Tie!!")
    player_score_label.config(text="Player Score: "+str(player_score))
    computer_score_label.config(text="Computer Score: "+str(computer_score))

def get_computer_choice():
    return random.choice(options)

def get_player_choice(player_input):
    global player_score, computer_score
    print(player_input)
    computer_input = get_computer_choice
    print(computer_input)
    player_choice_label.config(text="You Selected: "+player_input[0])
    computer_choice_label.config(text="Computer Selected: "+computer_input[0])
    
    if player_input == computer_input:
        tie()
    # if player selected rock 
    if(player_input[1] == 0): #0 represents rock 1 represents paper 2 represents scissors
        if(computer_input[1] == 1):
            computer_wins()
        elif(computer_input[1] == 2):
            player_wins()
            
    # if player selected paper        
    elif(player_input[1] == 1):
        if(computer_input[1] == 2):
            computer_wins()
        elif(computer_input[1] == 0):
            player_wins()
     
     # if player selected scissors 
    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        elif(computer_input[1] == 1):
            player_wins()

game_window = Tk()
game_window.title("Rock Paper Scissor game")

app_font = font.Font(size=12)

game_title = Label(text="Rock Paper Scissor")
game_title.pack()
winner_label = Label(text="Let's Start the Game", fg="Teal")
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame, text = "Your Options: ", font = app_font, fg = "grey")
player_options.pack()
#gridding
player_options.grid(row=0, column=0, pady=10)



rock_btn = Button(input_frame, text="Rock", bg="blue", fg="cyan", pady=8, command=lambda: get_player_choice(options[0]))
paper_btn = Button(input_frame, text="Paper", bg="green", fg="dark green", pady=8, command= lambda: get_player_choice(options[1]))
scissor_btn = Button(input_frame, text="Scissor", bg ="red", fg="dark red", pady=8, command=lambda: get_player_choice(options[2]))

rock_btn.grid(row = 1, column = 1, pady=10)
paper_btn.grid(row= 1, column = 2)



game_window.geometry("500x300")
game_window.mainloop()
            



