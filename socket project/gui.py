from tkinter import *

class GUI():
    def __init__(self, board):
        self.window = Tk()
        self.window.title("TicTacToe")

        self.load(board)
        self.window.mainloop()


    def load(self, board):
        btn1 = Button(self.window, text=board[0], height=5, width=10).grid(row=1, column=0)
        btn2 = Button(self.window, text=board[1], height=5, width=10).grid(row=2, column=0)
        btn3 = Button(self.window, text=board[2], height=5, width=10).grid(row=3, column=0)
        btn4 = Button(self.window, text=board[3], height=5, width=10).grid(row=1, column=1)
        btn5 = Button(self.window, text=board[4], height=5, width=10).grid(row=2, column=1)
        btn6 = Button(self.window, text=board[5], height=5, width=10).grid(row=3, column=1)
        btn7 = Button(self.window, text=board[6], height=5, width=10).grid(row=1, column=2)
        btn8 = Button(self.window, text=board[7], height=5, width=10).grid(row=2, column=2)
        btn9 = Button(self.window, text=board[8], height=5, width=10).grid(row=3, column=2)



