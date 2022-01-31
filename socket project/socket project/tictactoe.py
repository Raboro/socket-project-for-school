class TicTacToe():
    def __init__(self, client):
        self.header = "[TTT]"
        print(f"{self.header} Welcome to TicTacToe")
        client.send(bytes("\n[TICTACTOE] is starting\n", "utf-8"))