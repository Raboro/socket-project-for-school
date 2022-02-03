import time
import random

class GuessRandomNumber():
    def __init__(self, client):
        self.client = client
        self.header = "[GRN]"
        self.counter = 0
        print(f"{self.header} Welcome to GuessRandomNumber")
        client.send(bytes("\n[GUESSRANDOMNUMBER] is starting\n", "utf-8"))
        time.sleep(3)
        self.game()
        print("Stop GRN")
        self.client.close()

    def game(self):
        self.client.send(bytes(f"{self.header} guess a number between 0 and 100", "utf-8"))
        time.sleep(1)
        while True:


            self.random_number = random.randint(0, 100)
            while True:
                self.client.send(bytes(f"{self.header} Your guess:\n", "utf-8"))
                self.msg = self.client.recv(1024).decode("utf-8")
                self.msg = int(self.msg)

                if self.msg == self.random_number:
                    self.client.send(bytes(f"\n{self.header} Your right\n", "utf-8"))
                    time.sleep(2)
                    break

                elif self.msg > self.random_number:
                    self.client.send(bytes(f"{self.header} guess lower\n", "utf-8"))

                else:
                    self.client.send(bytes(f"{self.header} guess higher\n", "utf-8"))

                self.counter += 1

            print(f"{self.header} Your trys: {self.counter}")
            self.client.send(bytes(f"{self.header} Do you wanna play again [Yes/No]\n", "utf-8"))
            self.msg = self.client.recv(1024).decode("utf-8")
            if self.msg == "No":
                break
