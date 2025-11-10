class Singer:
    def __init__(self, name, song, relationship):
        self.name = name
        self.song = song
        self.relationship = relationship

    def greet(self):
        print(f"{self.name} says: Hello, how are you?")

    def sing(self):
        print(f"{self.name} sings {self.song} song.")

    def relation(self):
        print(f"{self.name} likes {self.relationship}")

nana = Singer("Nana", "Love like fire", "Zhangbing")
nana.greet()
nana.sing()
nana.relation()