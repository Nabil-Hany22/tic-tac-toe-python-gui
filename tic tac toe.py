import tkinter as tk
import random
import glob

# نافذة اللعبة
root = tk.Tk()
root.title("Tic-Tac-Toe Almdrasa")

player_score = 0
computer_score = 0


score_var = tk.StringVar()
status_var = tk.StringVar()

score_var.set(f"You: {player_score}   Computer: {computer_score}")
status_var.set("")

buttons = []


def load_result_message(result_type):
    pattern = f"assets/messages/{result_type}*.txt"
    files = glob.glob(pattern)
    if files:
        try:
            with open(files[0], 'r', encoding='utf-8') as f:
                message = f.read().strip()
                return message
        except:
            return f"{result_type.capitalize()}!"
    return f"{result_type.capitalize()}!"



def update_score(winner):
    global player_score, computer_score
    if winner == "X":
        player_score += 1
        msg = load_result_message("win")
        status_var.set(msg)
    elif winner == "O":
        computer_score += 1
        msg = load_result_message("lose")
        status_var.set(msg)
    elif winner == "Tie":
        msg = load_result_message("tie")
        status_var.set(msg)

    score_var.set(f"You: {player_score}   Computer: {computer_score}")



def check_winner():
    combos = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for combo in combos:
        values = [buttons[i]["text"] for i in combo]
        if values == ["X", "X", "X"]:
            for i in combo:
                buttons[i].config(bg="cyan")
            update_score("X")
            disable_buttons()
            return True
        elif values == ["O", "O", "O"]:
            for i in combo:
                buttons[i].config(bg="cyan")
            update_score("O")
            disable_buttons()
            return True
    if all(button["text"] != "" for button in buttons):
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
        btn.config(text="", state="normal", bg="SystemButtonFace")



def user_click(i):
    if buttons[i]["text"] == "" and status_var.get() == "":
        buttons[i].config(text="X")
        if not check_winner():
            root.after(500, computer_turn)



def computer_turn():
    empty_indices = [i for i in range(9) if buttons[i]["text"] == ""]
    if empty_indices:
        choice = random.choice(empty_indices)
        buttons[choice].config(text="O")
        check_winner()



tk.Label(root, textvariable=score_var, font=('Courier', 16)).pack(pady=10)
tk.Label(root, textvariable=status_var, font=('Courier', 20)).pack()

tk.Button(root, text="Restart", font=('Courier', 14), command=restart_game).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=('Courier', 32), width=5, height=2,
                    command=lambda i=i: user_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)


root.mainloop()
