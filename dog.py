class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)