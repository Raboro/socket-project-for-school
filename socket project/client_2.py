import socket
import time

class Client_2():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect(("127.0.0.1", 1112))
        self.msg = self.client.recv(1024).decode("utf-8")
        print(self.msg)
        self.name = input(f"<?> ~ ")
        self.stop = False
        self.client.send(self.name.encode("utf-8"))
        print("\n")
        self.run()
        print("See you soon, byee :)")
        time.sleep(3)

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
                if self.msg == "continue":
                    break
                else:
                    print("Something went wrong")
            except:
                pass

        while True:
            self.get_board()

            if self.stop == True:
                break

            while True:
                try:
                    self.msg = self.client.recv(1024).decode("utf-8")

                    if self.msg == "[TTT] Draw":
                        print(self.msg)
                        print("See you soon, byee :)")
                        self.stop = True
                        time.sleep(1)
                        break

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

                    elif self.msg == "[TTT] Winner":
                        print(self.msg)
                        quit()
                        self.stop = True
                        print("See you soon, byee :)")
                        time.sleep(1)
                        break

                    elif self.msg == "[TTT] Looser":
                        self.client.close()
                        print(self.msg)
                        quit()
                        self.stop = True
                        print("See you soon, byee :)")
                        time.sleep(1)
                        break

                except:
                    pass


if __name__ == "__main__":
    Client_2()