class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, "barks")

a = Animal("Generic")
d = Dog("Rex")

a.speak()
d.speak()