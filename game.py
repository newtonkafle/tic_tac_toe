## steps to categorize the player 1 and player 2
## find the win or lose
## calculate the score
## calculate the round
## reset the board when all the box is filled
import time
class Play:
    def __init__(self):
        self.round=None
        self.score = {'player_1': 0, 'player_2': 0}
        self.player= True
        self.box_list = []
        self.current_user = ''
        self.name = ['A', 'B', 'C']
        self.winner_cond = self.create_winner_condition()
        self.player_move = {"player_1" : [], "player_2" : []}

    """handles the function that need to be tigger after the click of the button"""
    def click(self, event):
        self.play_game(event)

        if self.check_winner():
            # increase the round
            self.round =+1
            # increase the score for the respective player
            self.score[self.current_user] += 1
            print(self.score)
            self.reset_board()

        if len(self.box_list) >= 9:
            time.sleep(2)
            self.reset_board()


    """create and handle a player moves with the special character for each player"""
    def play_game(self, event):
        button = event[0]
        if self.is_box_not_filled(button):
            self.box_list.append(event)
            if self.player:
                self.current_user = 'player_1'
                button.configure(text="X")
                button.configure(fg="red")
                self.player = False
            else:
                self.current_user = 'player_2'
                button.configure(text='O')
                button.configure(fg="blue")

                self.player = True
            self.player_move[self.current_user].append(event[1])

    """reset the box after successful attempt or draw"""
    def reset_board(self):
            for box in self.box_list:
                box[0].configure(text='')
                self.box_list=[]

            for key in self.player_move.keys():
                self.player_move[key] = []

    """return true if the box is not filled"""
    def is_box_not_filled(self, button):
        if button.cget('text') == '':
            return True
        return False

    """check the winner if the condition matches"""
    def check_winner(self):
        print(self.player_move)
        # returns true if condition matched with the user steps to win
        for cond in self.winner_cond:
            is_win =(all(item in self.player_move[self.current_user] for item in cond))
            print(is_win)
            if is_win:
                return is_win


    """creating the winner condition to check the winner"""
    def create_winner_condition(self):
        items=[]
        def get_condition(cond1, cond2, process=0):
            if process == 1:
                boxes = [f'{y}{x}' for x in cond1 for y in cond2]
            else:
                boxes = [f'{x}{y}' for x in cond1 for y in cond2]
            return [boxes[x:x+3] for x in range(0, len(boxes), 3)]

        items += get_condition(range(3), self.name, process=1)
        items += get_condition(self.name, range(3))

        items.append([f"{char}{num}" for num, char in enumerate(self.name)])
        items.append([f"{char}{2-num}" for num, char in enumerate(self.name)])
        print(items)
        return items


