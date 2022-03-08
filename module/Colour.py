
class Colour:

    R: int
    G: int
    B: int

    HEX: str

    def __init__(self) -> None:
        self.R = 0
        self.G = 0
        self.B = 0
        self.HEX = ""

    @staticmethod
    def parseColour(read):
        read = read.strip()
        read = read.split(":")
        return read

    def initColour(self, read):
        data = self.parseColour(read)
        id = ['R', 'G', 'B']
        values = [self.R, self.G, self.B]

        for i in range(len(id)):
            if id[i] == data[0]:
                values[i] = int(data[1])

        self.R = values[0]
        self.G = values[1]
        self.B = values[2]

    def getRGB(self):
        return self.R, self.G, self.B

    def getHEX(self):
        self.HEX = "#{:02x}{:02x}{:02x}".format(self.R, self.G, self.B)
        return self.HEX
