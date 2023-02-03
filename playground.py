import tkinter as tk
from tkinter import ttk

from Tic_Tac_Toe.game import Play
class Playground(tk.Tk, Play):
    def __init__(self):
        tk.Tk.__init__(self)
        Play.__init__(self)
        self.title('Tic Tac Toe')
        self.geometry('600x500')
        # Name of the game
        self.label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 25))
        self.label.grid(column=1, row=0)
        # self.play = Play()


        #Round
        self.round_lab = ttk.Label(self, text="Round: ", font=("Arial", 20))
        self.round_lab.grid(column=1, row=3)

        # player 1 label and score
        self.player1 = ttk.Label(self, text="Player 1", font=("Arial", 20, 'bold'))
        self.player1.grid(column=0, row=4)
        self.player1_score = ttk.Label(self, text=f"Score:0 ", font=("Arial", 15))
        self.player1_score.grid(column=0, row=5, sticky='w')


        # player 2 label and score
        self.player2 = ttk.Label(self, text="Player 2", font=("Arial", 20, 'bold'))
        self.player2.grid(column=2, row=4)
        self.player2_score = ttk.Label(self, text="Score:0", font=("Arial", 15))
        self.player2_score.grid(column=2, row=5, sticky='w')

        # creating label frame for playground
        self.ground_frame = ttk.LabelFrame(self)
        self.ground_frame.grid(column=1, row=2, padx=70, pady=30)

        #create playground
        self.button_list = {}
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.ground_frame, text="", height=2, width=2, font=('Arial', 35))
                button.configure(command= lambda m=(button, f'{self.name[row]}{col}'): [self.click(m), self.update_window()])
                button.grid(column=col, row=row)

    def update_window(self):
        self.player1_score.configure(text=f"score: {self.score['player_1']}")
        self.player2_score.configure(text=f"score: {self.score['player_2']}")
        self.round_lab.configure(text=f"Round: {self.round}")
        self.update()






