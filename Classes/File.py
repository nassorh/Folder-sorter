class File():
    def __init__(self):
        self.name = None
        self.path = None
        self.extension =None
        self.catergory = None
    
    def __str__(self):
        if self.catergory:
            return self.name + " " + self.catergory
        else:
            return self.name + " None"
