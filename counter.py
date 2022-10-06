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

# You found the hidden message.
# Please write your student ID in the following line of code and send the
# result to Google Classroom for evaluation.

student_id = b"65XXXXXXXX" # keep the quotes

if __name__ == "__main__":
    from hashlib import sha256
    print(sha256(student_id + b"asdfghjkl").hexdigest())
    c = Counter(100)
    c.up(100)
    c.down(200)
    print(c.get_value())
