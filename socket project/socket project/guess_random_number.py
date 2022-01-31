class GuessRandomNumber():
    def __init__(self, client):
        self.header = "[GRN]"
        print(f"{self.header} Welcome to GuessRandomNumber")
        client.send(bytes("\n[GUESSRANDOMNUMBER] is starting\n", "utf-8"))