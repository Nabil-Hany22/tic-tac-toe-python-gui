import tkinter as tk
import random

# ========= GLOBAL STATE ===========
player_symbol = "X"
computer_symbol = "O"
player_score = 0
computer_score = 0
buttons = []
theme = "light"

themes = {
    "light": {"bg": "SystemButtonFace", "fg": "black"},
    "dark": {"bg": "#2b2b2b", "fg": "white"}
}

# ========= FUNCTIONS ==============
def choose_symbol_and_theme():
    def apply_choices():
        global player_symbol, computer_symbol, theme
        player_symbol = symbol_var.get()
        computer_symbol = "O" if player_symbol == "X" else "X"
        theme = theme_var.get()
        apply_theme()
        choice_window.destroy()
        restart_game()
        if player_symbol == "O":
            root.after(500, computer_turn)

    choice_window = tk.Toplevel(root)
    choice_window.title("Game Setup")

    tk.Label(choice_window, text="Choose your symbol:", font=("Courier", 14)).pack(pady=10)
    symbol_var = tk.StringVar(value="X")
    tk.Radiobutton(choice_window, text="X", variable=symbol_var, value="X").pack()
    tk.Radiobutton(choice_window, text="O", variable=symbol_var, value="O").pack()

    tk.Label(choice_window, text="Choose theme:", font=("Courier", 14)).pack(pady=10)
    theme_var = tk.StringVar(value="light")
    tk.Radiobutton(choice_window, text="Light", variable=theme_var, value="light").pack()
    tk.Radiobutton(choice_window, text="Dark", variable=theme_var, value="dark").pack()

    tk.Button(choice_window, text="Start Game", command=apply_choices).pack(pady=10)

def apply_theme():
    root.configure(bg=themes[theme]["bg"])
    score_label.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    status_label.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    for btn in buttons:
        btn.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])
    restart_btn.configure(bg=themes[theme]["bg"], fg=themes[theme]["fg"])

def update_score(winner):
    global player_score, computer_score
    if winner == player_symbol:
        player_score += 1
        status_var.set(f"{player_symbol} wins!")
    elif winner == computer_symbol:
        computer_score += 1
        status_var.set(f"{computer_symbol} wins!")
    elif winner == "Tie":
        status_var.set("It's a tie!")
    score_var.set(f"You: {player_score}   Computer: {computer_score}")

def check_winner():
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for combo in combos:
        values = [buttons[i]["text"] for i in combo]
        if values == [player_symbol]*3 or values == [computer_symbol]*3:
            for i in combo:
                buttons[i].config(bg="cyan")
            update_score(values[0])
            disable_buttons()
            return True
    if all(btn["text"] != "" for btn in buttons):
        for btn in buttons:
            btn.config(bg="red")
        update_score("Tie")
        return True
    return False

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def restart_game():
    status_var.set("")
    for btn in buttons:
        btn.config(text="", state="normal", bg=themes[theme]["bg"], fg=themes[theme]["fg"])

def user_click(i):
    if buttons[i]["text"] == "" and status_var.get() == "":
        buttons[i].config(text=player_symbol)
        if not check_winner():
            root.after(500, computer_turn)

def computer_turn():
    empty = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty:
        move = random.choice(empty)
        buttons[move].config(text=computer_symbol)
        check_winner()

# ========== GUI SETUP ============
root = tk.Tk()
root.title("Tic-Tac-Toe")

score_var = tk.StringVar()
status_var = tk.StringVar()
score_var.set(f"You: {player_score}   Computer: {computer_score}")
status_var.set("")

score_label = tk.Label(root, textvariable=score_var, font=("Courier", 16))
score_label.pack(pady=10)

status_label = tk.Label(root, textvariable=status_var, font=("Courier", 20))
status_label.pack()

restart_btn = tk.Button(root, text="Restart", font=("Courier", 14), command=choose_symbol_and_theme)
restart_btn.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Courier", 32), width=5, height=2,
                    command=lambda i=i: user_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Ask at launch
root.after(100, choose_symbol_and_theme)

root.mainloop()
