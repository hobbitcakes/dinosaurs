class Creature():

    def __init__(self, kind="Creature", name="Eve"):
        self.kind = kind
        self.name = name
        self.voice = "Hrmmmph"

    def __repr__():
        return f'Type: {self.kind}\nName: {self.name}'


    def speak() -> str:
        return self.voice

