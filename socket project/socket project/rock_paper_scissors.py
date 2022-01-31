class RockPaperScissors():
    def __init__(self, client):
        self.header = "[RPS]"
        print(f"{self.header} Welcome to RockPaperScissors")
        client.send(bytes("\n[ROCKPAPERSCICCORS] is starting\n", "utf-8"))