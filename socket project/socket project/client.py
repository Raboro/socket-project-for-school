import socket
import time


class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect(("127.0.0.1", 55555))
        self.msg = self.client.recv(1024).decode("utf-8")
        print(self.msg)
        self.name = input(f"<?> ~ ")
        self.stop = False
        self.client.send(self.name.encode("utf-8"))
        print("")
        for i in range(6):
            print("[WAITING]")
            time.sleep(0.5)
        print("\n")
        self.run()

    def run(self):
        while True:
            try:
                self.msg = self.client.recv(1024).decode("utf-8")
                if self.msg == "[SERVER] You can choose between the games: [1 TICTACTOE][2 GuessRandomNumber][3 RockPaperScissors] -> [1, 2, 3]":
                    print(f"{self.msg}\n")
                    while True:
                        self.response = input(f"<{self.name}> ~ ")
                        if self.response in ["1", "2", "3"]:
                            break
                        else:
                            print("Please select a game\n")
                    self.client.send(bytes(self.response, "utf-8"))

                # TicTacToe
                if self.msg == "\n[TICTACTOE] is starting\n":
                    print(self.msg)

                # GuessRandomNumber
                elif self.msg == "\n[GUESSRANDOMNUMBER] is starting\n":
                    print(self.msg)

                # RockPaperScissors
                elif self.msg == "\n[ROCKPAPERSCICCORS] is starting\n":
                    print(self.msg)

                # continue or quit
                if self.msg == "[SERVER] Continue [Yes/No]":
                    print(f"{self.msg}\n")
                    while True:
                        self.response = input(f"<{self.name}> ~ ")
                        if self.response in ["Yes", "No"]:
                            if self.response == "No":
                                self.stop = True
                            self.client.send(bytes(self.response, "utf-8"))
                            break
                        else:
                            print("That doesen´t work\n")

                if self.stop == True:
                    print("See you soon, byee :)")
                    time.sleep(1)
                    break

            except:
                print("Something went wrong")

if __name__ == "__main__":
    Client()