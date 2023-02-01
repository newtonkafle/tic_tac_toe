import tkinter as tk
from tkinter import ttk
class Playground(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.geometry('600x500')
        # Name of the game
        self.label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 25))
        self.label.grid(column=1, row=0)


        #Round
        self.label = ttk.Label(self, text="Round: ", font=("Arial", 20))
        self.label.grid(column=1, row=3)

        # player 1 label and score
        self.player1 = ttk.Label(self, text="Player 1", font=("Arial", 20, 'bold'))
        self.player1.grid(column=0, row=4)
        self.player1_score = ttk.Label(self, text="Score:", font=("Arial", 15))
        self.player1_score.grid(column=0, row=5, sticky='w')


        # player 2 label and score
        self.player2 = ttk.Label(self, text="Player 2", font=("Arial", 20, 'bold'))
        self.player2.grid(column=2, row=4)
        self.player2_score = ttk.Label(self, text="Score:", font=("Arial", 15))
        self.player2_score.grid(column=2, row=5, sticky='w')

        # creating label frame for playground
        self.ground_frame = ttk.LabelFrame(self)
        self.ground_frame.grid(column=1, row=2, padx=70, pady=30)

        #create playground
        self.name = ['A', 'B', 'C']
        self.names_dic = {}
        for row in range(3):
            for col in range(3):
                self.names_dic[f"{self.name[row]}{col}"] = ttk.Label(self.ground_frame, text='__', borderwidth=1, relief='solid',
                             font=('Arial', 80))
                self.names_dic[f"{self.name[row]}{col}"].grid(column=col, row=row)





