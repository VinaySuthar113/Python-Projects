from customtkinter import *
import random

def get_player_names():
    global player1_name, player2_name

    name_window = CTkToplevel(window)
    name_window.geometry("250x250")
    name_window.title("Enter Player Names")

    label1 = CTkLabel(master=name_window, text="Player 1 (X):", font=CTkFont("Permanent Marker", size=20))
    label1.pack(pady=5)
    entry1 = CTkEntry(master=name_window, font=CTkFont("Permanent Marker", size=20))
    entry1.pack(pady=5)

    label2 = CTkLabel(master=name_window, text="Player 2 (O):", font=CTkFont("Permanent Marker", size=20))
    label2.pack(pady=5)
    entry2 = CTkEntry(master=name_window, font=CTkFont("Permanent Marker", size=20))
    entry2.pack(pady=5)

    def on_confirm():
        global player1_name, player2_name, player_scores, player
        player1_name = entry1.get()
        player2_name = entry2.get()
        player_scores = {player1_name: 0, player2_name: 0}
        player = random.choice([player1_name, player2_name])
        player_label.configure(text=f"{player1_name} (X) vs {player2_name} (O)")
        label.configure(text=f"{player}'s turn")
        name_window.destroy()

    confirm_button = CTkButton(master=name_window, text="Confirm", command=on_confirm, font=CTkFont("Permanent Marker", size=20))
    confirm_button.pack(pady=20)

    name_window.grab_set()
    window.wait_window(name_window)
    
def next_turn(row, column):
    global player

    if buttons[row][column].cget('text') == "" and check_winner() is False:
        buttons[row][column].configure(text='X' if player == player1_name else 'O')

        if check_winner() is False:
            player = player2_name if player == player1_name else player1_name
            label.configure(text=(player + "'s turn"))

        elif check_winner() is True:
            label.configure(text=(player + " wins!"))
            player_scores[player] += 1
            update_score()

        elif check_winner() == "Tie":
            label.configure(text="Tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0].cget('text') == buttons[row][1].cget('text') == buttons[row][2].cget('text') != "":
            buttons[row][0].configure(fg_color="red")
            buttons[row][1].configure(fg_color="red")
            buttons[row][2].configure(fg_color="red")
            return True

    for column in range(3):
        if buttons[0][column].cget('text') == buttons[1][column].cget('text') == buttons[2][column].cget('text') != "":
            buttons[0][column].configure(fg_color="red")
            buttons[1][column].configure(fg_color="red")
            buttons[2][column].configure(fg_color="red")
            return True

    if buttons[0][0].cget('text') == buttons[1][1].cget('text') == buttons[2][2].cget('text') != "":
        buttons[0][0].configure(fg_color="red")
        buttons[1][1].configure(fg_color="red")
        buttons[2][2].configure(fg_color="red")
        return True

    if buttons[0][2].cget('text') == buttons[1][1].cget('text') == buttons[2][0].cget('text') != "":
        buttons[0][2].configure(fg_color="red")
        buttons[1][1].configure(fg_color="red")
        buttons[2][0].configure(fg_color="red")
        return True

    if empty_spaces() is False:
        return "Tie"

    return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column].cget('text') != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice([player1_name, player2_name])
    label.configure(text=player + "'s turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].configure(text="", fg_color="gray")

def update_score():
    score_label.configure(text=f"{player1_name}: {player_scores[player1_name]} | {player2_name}: {player_scores[player2_name]}")

window = CTk()
window.title("Tic-Tac-Toe")
window.resizable(False, False)

player1_name = "Player 1"
player2_name = "Player 2"
player_scores = {player1_name: 0, player2_name: 0}
player = random.choice([player1_name, player2_name])

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = CTkLabel(master=window, text=player + "'s turn", font=CTkFont("Permanent Marker", size=40))
label.pack(side=TOP)

reset_button = CTkButton(master=window, text="Restart", font=CTkFont("Permanent Marker", size=20), command=new_game)
reset_button.pack(side=TOP)

frame = CTkFrame(master=window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = CTkButton(master=frame, text="", font=CTkFont("Permanent Marker", size=40), width=150, height=100, fg_color="gray", command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column, padx=5, pady=5)

player_label = CTkLabel(master=window, text=f"{player1_name} (X) vs {player2_name} (O)", font=CTkFont("Permanent Marker", size=20))
player_label.pack(side=TOP)

score_label = CTkLabel(master=window, text=f"{player1_name}: 0 | {player2_name}: 0", font=CTkFont("Permanent Marker", size=20))
score_label.pack(side=TOP)

get_player_names()

window.mainloop()
