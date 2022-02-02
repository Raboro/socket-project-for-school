import time

class TicTacToe():
    def __init__(self, client, server, name):
        self.client = client
        self.server = server
        self.name_client = name
        self.header = "[TTT]"
        print(f"{self.header} Welcome to TicTacToe")
        self.client.send(bytes("\n[TICTACTOE] is starting\n", "utf-8"))
        time.sleep(3)
        self.board_elements = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.client.send(bytes("\n[TTT] do you wanna play against a player or against the server [player/server]\n", "utf-8"))
        self.mode = client.recv(1024).decode("utf-8")
        if self.mode == "player":
            print("[TTT] Multiplayer selected")
            self.multiplayer()
        else:
            print("[TTT] Singleplayer selected")
            self.singleplayer()
        print("Stop TTT")

    def send_board(self):
        self.board = [
            "\nCurrend Board:\n",
            " -------------",
            f" | {self.board_elements[0]} | {self.board_elements[1]} | {self.board_elements[2]} |",
            " |-----------|",
            f" | {self.board_elements[3]} | {self.board_elements[4]} | {self.board_elements[5]} |",
            " |-----------|",
            f" | {self.board_elements[6]} | {self.board_elements[7]} | {self.board_elements[8]} |",
            " -------------\n"
        ]

        for i in self.board:
            self.client.send(bytes(i, "utf-8"))
            self.client_2.send(bytes(i, "utf-8"))
            time.sleep(0.5)

    def load_board(self):
        self.board = [
            "\nCurrend Board:\n",
            " -------------",
            f" | {self.board_elements[0]} | {self.board_elements[1]} | {self.board_elements[2]} |",
            " |-----------|",
            f" | {self.board_elements[3]} | {self.board_elements[4]} | {self.board_elements[5]} |",
            " |-----------|",
            f" | {self.board_elements[6]} | {self.board_elements[7]} | {self.board_elements[8]} |",
            " -------------\n"
        ]

    def set_position(self, character):
        print(character)
        if self.board_elements[self.position] == " ":
            self.board_elements[self.position] = character
        else:
            print(f"{self.header} Wrong move, whats wrong with you")

        self.load_board()
        for i in self.board:
            print(i)


    def check_if_winner(self):
        print("check")
        # Hor.
        if self.board_elements[0] == self.board_elements[1] and self.board_elements[0] == self.board_elements[2] and self.board_elements[0] in ["X", "O"] :
            print(f"{self.header} WINNER")
            return self.board_elements[0]

        elif self.board_elements[3] == self.board_elements[4] and self.board_elements[3] == self.board_elements[5] and self.board_elements[3] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[3]

        elif self.board_elements[6] == self.board_elements[7] and self.board_elements[6] == self.board_elements[8] and self.board_elements[6] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[6]

        # Ver.
        elif self.board_elements[0] == self.board_elements[3] and self.board_elements[0] == self.board_elements[6] and self.board_elements[0] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[0]

        elif self.board_elements[1] == self.board_elements[4] and self.board_elements[1] == self.board_elements[7] and self.board_elements[1] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[1]

        elif self.board_elements[2] == self.board_elements[5] and self.board_elements[2] == self.board_elements[8] and self.board_elements[2] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[2]

        # qu.
        elif self.board_elements[0] == self.board_elements[4] and self.board_elements[0] == self.board_elements[8] and self.board_elements[3] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[0]

        elif self.board_elements[2] == self.board_elements[4] and self.board_elements[2] == self.board_elements[6] and self.board_elements[3] in ["X", "O"]:
            print(f"{self.header} WINNER")
            return self.board_elements[2]

        return ""


    def if_winner(self):
        if self.is_winner == "X":
            print(f"{self.header} {self.name_client} is the winner")
            self.client.send(bytes(f"{self.header} Winner", "utf-8"))
            self.client_2.send(bytes(f"{self.header} Looser", "utf-8"))
        else:
            print(f"{self.header} {self.name_client_2} is the winner")
            self.client_2.send(bytes(f"{self.header} Winner", "utf-8"))
            self.client.send(bytes(f"{self.header} Looser", "utf-8"))

    def multiplayer(self):
        print(f"{self.header} Waiting for second player")
        while True:
            self.client_2, self.address = self.server.accept()
            print(f"{self.header} new connection {self.address}")
            self.client_2.send(bytes("[SERVER] Welcome to the Server\nEnter your name:", "utf-8"))
            self.name_client_2 = self.client_2.recv(1024).decode("utf-8")
            break

        print(f"{self.header} Player:\n{self.header} {1}: {self.name_client}\n{self.header} {2}: {self.name_client_2}\n")
        self.client.send(bytes("continue", "utf-8"))
        self.client_2.send(bytes("continue", "utf-8"))
        time.sleep(2)
        print(f"{self.header} game starting")

        self.player = 1
        self.is_winner = ""
        while True:
            self.send_board()

            if self.player == 1:
                self.client.send(bytes(f"{self.header} choose a field:", "utf-8"))
                self.client_2.send(bytes(f"{self.header} not you", "utf-8"))
                self.position = self.client.recv(1024).decode("utf-8")
                self.position = int(self.position)-1
                self.set_position("X")
                self.is_winner = self.check_if_winner()
                if self.is_winner !=  "":
                    self.if_winner()
                    break
                self.player = 2

            elif self.player == 2:
                self.client_2.send(bytes(f"{self.header} choose a field:", "utf-8"))
                self.client.send(bytes(f"{self.header} not you", "utf-8"))
                self.position = self.client_2.recv(1024).decode("utf-8")
                self.position = int(self.position) - 1
                self.set_position("O")
                self.is_winner = self.check_if_winner()
                if self.is_winner !=  "":
                    self.if_winner()
                    break
                self.player = 1

        time.sleep(3)
        #self.client_2.close()
        print("Stop Mutli")


    def singleplayer(self):
        pass

    def return_client(self):
        return self.client