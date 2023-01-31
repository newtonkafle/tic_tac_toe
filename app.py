import tkinter as tk

# project approach for tictactoe

# first create a gui interface
#create the logic for player turn
# create the login for winning the session

# three successful circle or cross within the same row or same column or diagonally should win the session
# continue to run the game after wining creating a player score

class TicTacToc(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.geometry('800x500')



if __name__ == "__main__":
    app = TicTacToc()
    app.mainloop()


