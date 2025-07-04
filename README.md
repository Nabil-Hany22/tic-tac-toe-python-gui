# ❌⭕ Tic Tac Toe Game (Python GUI Project)

This is my **final project** required to complete the course:

🎓 **[Programming Foundations using Python](https://almdrasa.com/tracks/programming-foundations-track)** offered by [Almdrasa](https://almdrasa.com)

By building this project, I practiced my understanding of **GUI programming** using `tkinter`, along with logic handling, file management, and user interaction design. I submitted this as the final required task for the course.

---

## 🧠 Project Overview

This game allows the player to play Tic-Tac-Toe against the computer. The computer makes **random choices**, and the player can track wins/losses during the game.

The application includes:

* A 3x3 game board using buttons
* Score tracking: player vs computer
* Randomized AI opponent
* GUI built using `tkinter`
* Enhanced version with:

  * Dark and Light mode support
  * Symbol selection (X or O)
  * Smart game restart and theming

---

## 📂 Files in the Repository

| File                           | Description                                       |
| ------------------------------ | ------------------------------------------------- |
| `tic tac toe.py`               | Basic version of the game                         |
| `tic tac toe_chatgpt.py`       | Enhanced version with themes and symbol selection |
| `tic tac toe planning.jpg`     | Visual plan / layout of the game interface        |
| `assets/messages/win_msg.txt`  | Custom win message                                |
| `assets/messages/lose_msg.txt` | Custom lose message                               |
| `assets/messages/tie_msg.txt`  | Custom tie message                                |

---

## 🕹️ Controls in the Game

| Control Name        | Type    | Example                     |
| ------------------- | ------- | --------------------------- |
| Score               | Label   | `You: 3   Computer: 5`      |
| Restart             | Button  | `Restart`                   |
| Win/Lose/Tie Status | Label   | `X wins!`, `O wins!`, `Tie` |
| Game Grid           | Buttons | 3x3 grid                    |

---

## 🔥 Enhanced Features

### 🔸 Basic Version – `tic tac toe.py`

* GUI using `tkinter`
* Random computer moves
* Score tracking
* Reads win/lose/tie messages from `.txt` files using `glob`

### ⚡ Enhanced Version – `tic tac toe_chatgpt.py`

* All basic features, plus:

  * ✅ Choose your symbol (X or O)
  * ✅ Dark Mode / Light Mode switch
  * ✅ Computer plays first if player chooses "O"
  * ✅ Cleaner layout and separation of concerns

---

## 🧠 What I Learned

* GUI design using `tkinter`
* Creating interactive games with Python
* Using `glob` to dynamically load files
* Structuring project files and folders
* Improving user experience with personalization (theme/symbol)
* Managing game logic, events, and visual feedback

---

## 🧰 Tech Stack

* `Python 3.7+`
* `tkinter` for GUI
* `random` for AI moves
* `glob` for loading result messages

---

## 📸 Planning & Visuals

See `tic tac toe planning.jpg` for the original layout and component planning.

---

## ✅ Run the Project

Make sure you have Python 3.7 or above installed, then run:

```bash
python "tic tac toe.py"
# or
python "tic tac toe_chatgpt.py"
```

---




