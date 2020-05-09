class Entity:
    #a generic to represent players, enemies items etc

    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    #handle the entitys movement
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
