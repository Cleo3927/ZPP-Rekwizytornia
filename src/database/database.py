class Database():
    def __init__(self):
        self.last_element = 1

    def get_index(self):
        return self.last_element

    def add_element(self):
        self.last_element += 1

