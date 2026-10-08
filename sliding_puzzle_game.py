"""Sliding Puzzle (15-puzzle) in Python with Tkinter.
No installs needed. Run: python puzzle_game.py
"""
import random
import tkinter as tk

SIZE = 4  # change to 3 for an easier 8-puzzle


class Puzzle:
    def __init__(self, root):
        root.title("Sliding Puzzle")
        self.label = tk.Label(root, text="Moves: 0", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=SIZE, pady=6)

        self.buttons = []
        for i in range(SIZE * SIZE):
            b = tk.Button(
                root, font=("Arial", 20, "bold"), width=4, height=2,
                command=lambda i=i: self.click(i),
            )
            b.grid(row=i // SIZE + 1, column=i % SIZE, padx=1, pady=1)
            self.buttons.append(b)

        tk.Button(root, text="New Game", command=self.new_game).grid(
            row=SIZE + 1, column=0, columnspan=SIZE, pady=8
        )
        self.new_game()

    def neighbors(self, i):
        r, c = divmod(i, SIZE)
        out = []
        if r > 0: out.append(i - SIZE)
        if r < SIZE - 1: out.append(i + SIZE)
        if c > 0: out.append(i - 1)
        if c < SIZE - 1: out.append(i + 1)
        return out

    def new_game(self):
        # Start solved, then make random legal moves -> always solvable
        self.tiles = list(range(1, SIZE * SIZE)) + [0]
        blank = SIZE * SIZE - 1
        for _ in range(300):
            n = random.choice(self.neighbors(blank))
            self.tiles[blank], self.tiles[n] = self.tiles[n], self.tiles[blank]
            blank = n
        self.moves = 0
        self.draw()

    def click(self, i):
        blank = self.tiles.index(0)
        if blank in self.neighbors(i):
            self.tiles[blank], self.tiles[i] = self.tiles[i], self.tiles[blank]
            self.moves += 1
            self.draw()

    def draw(self):
        solved = self.tiles == list(range(1, SIZE * SIZE)) + [0]
        for b, t in zip(self.buttons, self.tiles):
            b.config(
                text="" if t == 0 else str(t),
                state="disabled" if solved or t == 0 else "normal",
                bg="#f0f0f0" if t == 0 else "#4a90d9",
                fg="white",
            )
        if solved:
            self.label.config(text=f"You won in {self.moves} moves!")
        else:
            self.label.config(text=f"Moves: {self.moves}")


if __name__ == "__main__":
    root = tk.Tk()
    Puzzle(root)
    root.mainloop()
