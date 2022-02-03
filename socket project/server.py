import socket
import time
from rock_paper_scissors import *
from guess_random_number import *
from tictactoe import *


class Server():
    def __init__(self):
        self.game_options = {
            "1": self.TicTacToe,
            "2": self.GuessRandomNumber,
            "3": self.RockPaperScissors
        }

        self.continue_after_player = False
        self.player = []
        self.host = "127.0.0.1"
        self.port = 1112
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print("[STARTING SERVER]")
        self.PlayerConnection()
        self.choose_game()


    def PlayerConnection(self):
        while True:
            self.client, self.address = self.server.accept()
            print(f"[SERVER] new connection {self.address}")
            self.client.send(bytes("[SERVER] Welcome to the Server\nEnter your name:", "utf-8"))
            self.name = self.client.recv(1024).decode("utf-8")
            break

    def TicTacToe(self):
        print("[SERVER] TicTacToe selected")
        print("[SERVER] waiting....")
        time.sleep(2)
        print("[...]")
        time.sleep(1)
        self.ttt_game = TicTacToe(self.client, self.server, self.name)

    def GuessRandomNumber(self):
        print("[SERVER] GuessRandomNumber selected")
        print("[SERVER] waiting....")
        time.sleep(2)
        print("[...]")
        time.sleep(1)
        self.grn_game = GuessRandomNumber(self.client)

    def RockPaperScissors(self):
        print("[SERVER] RockPaperScissors selected")
        print("[SERVER] waiting....")
        time.sleep(2)
        print("[...]")
        time.sleep(1)
        self.rpc_game = RockPaperScissors(self.client)

    def choose_game(self):
        self.msg = "[SERVER] You can choose between the games: [1 TICTACTOE][2 GuessRandomNumber][3 RockPaperScissors] -> [1, 2, 3]"
        while True:
            self.client.send(bytes(self.msg, "utf-8"))
            self.response = self.client.recv(1024).decode("utf-8")
            if self.response in ["1", "2", "3"]:
                break

        self.game_options[self.response]()

        print("[SERVER] Game closed")
        time.sleep(2)
        print("[SERVER] clossing")


if __name__ == "__main__":
    Server()
    quit()