""" Counter """

class Counter:
    def __init__(self, start_value=0):
        self.value = start_value

    def up(self, by=1):
        self.value += by

    def down(self, by=1):
        self.value -= by

    def get_value(self):
        return self.value

if __name__ == "__main__":
    c = Counter(100)
    c.up(100)
    c.down(200)
    print(c.get_value())
