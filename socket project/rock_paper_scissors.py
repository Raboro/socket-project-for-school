import time
import random

class RockPaperScissors():
    def __init__(self, client):
        self.client = client
        self.game_board = [0, 0]
        self.header = "[RPS]"
        print(f"{self.header} Welcome to RockPaperScissors")
        client.send(bytes("\n[ROCKPAPERSCICCORS] is starting\n", "utf-8"))
        self.game()


    def get_characters(self, rn, msg):
        player = [rn, msg]
        new_player = []
        for i in player:
            if i == 0:
                new_player.append("Rock")
            elif i == 1:
                new_player.append("Paper")
            else:
                new_player.append("Scissors")
        return new_player[0], new_player[1]


    def who_is_winner(self, s, c):
        if s == "Rock" and c == "Scissors":
            return "Server"
        elif s == "Paper" and c == "Rock":
            return "Server"
        elif s == "Scissors" and c == "Paper":
            return "Server"

        elif c == "Rock" and s == "Scissors":
            return "Client"
        elif c == "Paper" and s == "Rock":
            return "Client"
        elif c == "Scissors" and s == "Paper":
            return "Client"

        return "Nobody"


    def load_game_board(self, w):
        if w == "Client":
            self.game_board[0] += 1
        elif w == "Server":
            self.game_board[1] += 1


    def game(self):
        self.client.send(bytes(f"{self.header} take rock, paper or scissors\n", "utf-8"))
        time.sleep(1)
        while True:
            self.random_number = random.randint(0, 2)
            while True:
                self.client.send(bytes(f"{self.header} Lets play; choose [Rock|Paper|Scissors] -> [1|2|3]:\n", "utf-8"))
                self.msg = self.client.recv(1024).decode("utf-8")
                self.msg = int(self.msg)-1
                s_character, c_character = self.get_characters(self.random_number, self.msg)
                print(f"{self.header} You choose {c_character}")
                print(f"{self.header} Server choose {s_character}")
                winner = self.who_is_winner(s_character, c_character)
                print(f"\n{self.header} {winner} is the winner")
                self.load_game_board(winner)

                print(f"\n {self.game_board[0]} : {self.game_board[1]}\n")
                break


            self.client.send(bytes(f"\n{self.header} Do you wanna play again [Yes/No]\n", "utf-8"))
            self.msg = self.client.recv(1024).decode("utf-8")
            if self.msg == "No":
                break