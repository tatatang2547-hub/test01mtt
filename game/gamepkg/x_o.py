import tkinter as tk
from tkinter import messagebox


class TicTacToeUI:

    def __init__(self, root):
        self.root = root
        self.root.title("เกม XO (Tic-Tac-Toe)")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.status_label = tk.Label(
            self.root,
            text=f"ตาของผู้เล่น: {self.current_player}",
            font=("Helvetica", 14, "bold"),
            padx=10,
            pady=10,
        )
        self.status_label.pack()

        self.grid_frame = tk.Frame(self.root, bg="#333333", padx=5, pady=5)
        self.grid_frame.pack()

        self.create_buttons()

        self.reset_button = tk.Button(
            self.root,
            text="เริ่มเกมใหม่ 🔄",
            font=("Helvetica", 12),
            command=self.reset_game,
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            padx=10,
            pady=5,
        )
        self.reset_button.pack(pady=10)

    def create_buttons(self):
        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=("Helvetica", 24, "bold"),
                width=5,
                height=2,
                bg="#ffffff",
                relief="flat",
                command=lambda idx=i: self.on_button_click(idx),
            )
            btn.grid(row=row, column=col, padx=3, pady=3)
            self.buttons.append(btn)

    def on_button_click(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            color = "#1E88E5" if self.current_player == "X" else "#E53935"
            self.buttons[index].config(text=self.current_player, fg=color)

            if self.check_winner():
                self.status_label.config(
                    text=f"🎉 ผู้เล่น {self.current_player} ชนะ!",
                    fg="#4CAF50",
                )
                messagebox.showinfo(
                    "จบเกม", f"ยินดีด้วย! ผู้เล่น {self.current_player} ชนะ!"
                )
            elif "" not in self.board:
                self.status_label.config(text="🤝 เสมอกัน!", fg="#FB8C00")
                messagebox.showinfo("จบเกม", "เสมอ! ไม่มีใครชนะ")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(
                    text=f"ตาของผู้เล่น: {self.current_player}", fg="black"
                )

    def check_winner(self):
        win_conditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for cond in win_conditions:
            if (
                self.board[cond[0]]
                == self.board[cond[1]]
                == self.board[cond[2]]!= ""
            ):
                for idx in cond:
                    self.buttons[idx].config(bg="#C8E6C9")
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.status_label.config(
            text=f"ตาของผู้เล่น: {self.current_player}", fg="black"
        )
        for btn in self.buttons:
            btn.config(text="", bg="#ffffff")


def start_game():
    """ฟังก์ชันหลักสำหรับเริ่มรันเกม XO"""
    root = tk.Tk()
    game = TicTacToeUI(root)
    root.mainloop()