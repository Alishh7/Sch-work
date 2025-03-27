class Friend(object):
    def __init__(self, name, friendship):
        self.name = name
        self.friendship = friendship
    
    def get_name(self):
        return self.name
    
    def get_friendship(self):
        return self.friendship
    
    def chat(self):
        print("you talked to your friend")
        self.friendship = self.friendship + 20

    def fight(self):
        print("you argued with your friend")
        self.friendship = self.friendship - 20

    def slap(self):
        print("you slapped your friend")
        self.friendship = self.friendship - 15

    def hug(self):
        print("you hugged your friend")
        self.friendship = self.friendship + 50

    def rightHookToTheJaw(self):
        print("you gave your friend a right hook to the jaw")
        self.friendship = self.friendship - 100
