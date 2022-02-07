import socket
import time


class Client():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect(("127.0.0.1", 1112))
        self.msg = self.client.recv(1024).decode("utf-8")
        print(self.msg)
        self.name = input(f"<?> ~ ")
        self.client.send(self.name.encode("utf-8"))
        print("")
        for i in range(6):
            print("[WAITING]")
            time.sleep(0.5)
        print("\n")
        self.run()

    def get_board(self):
        for i in range(8):
            while True:
                try:
                    self.msg = self.client.recv(1024).decode("utf-8")
                    print(self.msg)
                    break
                except:
                    pass

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

                    while True:
                        try:
                            self.msg = self.client.recv(1024).decode("utf-8")
                            if self.msg == "continue":
                                break
                            else:
                                print("Something went wrong")
                        except:
                            pass

                    while True:
                        self.get_board()

                        while True:
                            try:
                                self.msg = self.client.recv(1024).decode("utf-8")

                                if self.msg == "[TTT] not you":
                                    print("\n[TTT] waiting for the other player\n")
                                    break

                                elif self.msg == "[TTT] choose a field:":
                                        print(self.msg)
                                        while True:
                                            self.response = input(f"<{self.name}> ~ ")
                                            if self.response in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                                self.client.send(bytes(self.response, "utf-8"))
                                                break
                                            else:
                                                print("Please type a correct answer\n")

                            except:
                                pass

                # GuessRandomNumber
                elif self.msg == "\n[GUESSRANDOMNUMBER] is starting\n":
                    print(self.msg)
                    while True:
                        try:
                            self.msg = self.client.recv(1024).decode("utf-8")
                            print(self.msg)
                            break
                        except:
                            pass

                    while True:
                        while True:
                            try:
                                self.msg = self.client.recv(1024).decode("utf-8")


                                if self.msg == "[GRN] Your guess:\n":
                                    print(self.msg)
                                    while True:
                                        self.response = int(input(f"<{self.name}> ~ "))
                                        if self.response <= 100:
                                            self.client.send(bytes(str(self.response), "utf-8"))
                                            break
                                        else:
                                            print("Please type a correct answer\n")

                                elif self.msg == "\n[GRN] Your right\n":
                                    print(self.msg)
                                    break

                                else:
                                    print(self.msg)


                            except:
                                pass

                        try:
                            self.msg = self.client.recv(1024).decode("utf-8")
                            print(self.msg)

                            while True:
                                self.response = input(f"<{self.name}> ~ ")
                                if self.response in ["Yes", "No"]:
                                    self.client.send(bytes(self.response, "utf-8"))
                                    break
                                else:
                                    print("Please type a correct answer\n")

                            if self.response == "No":
                                print("See you soon, byee :)")
                                time.sleep(1)
                                break
                        except:
                            pass

                # RockPaperScissors
                elif self.msg == "\n[ROCKPAPERSCICCORS] is starting\n":
                    print(self.msg)
                    while True:
                        try:
                            self.msg = self.client.recv(1024).decode("utf-8")
                            print(self.msg)
                            break
                        except:
                            pass

                    while True:
                        while True:
                            try:
                                self.msg = self.client.recv(1024).decode("utf-8")
                                print(self.msg)
                                while True:
                                    self.response = input(f"<{self.name}> ~ ")
                                    if self.response in ["1", "2", "3"]:
                                        self.client.send(bytes(self.response, "utf-8"))
                                        break
                                    else:
                                        print("Please type a correct answer\n")
                                break

                            except:
                                pass

                        try:
                            self.msg = self.client.recv(1024).decode("utf-8")
                            print(self.msg)

                            while True:
                                self.response = input(f"<{self.name}> ~ ")
                                if self.response in ["Yes", "No"]:
                                    self.client.send(bytes(self.response, "utf-8"))
                                    break
                                else:
                                    print("Please type a correct answer\n")



                        except:
                            pass

                        if self.response == "No":
                            print("See you soon, byee :)")
                            time.sleep(1)
                            break


            except:
                print("Something went wrong")

if __name__ == "__main__":
    Client()