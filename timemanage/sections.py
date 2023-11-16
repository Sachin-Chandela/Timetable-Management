class sections:
    def __init__(self,lecture_name,day=[],slot=[]):
        self.lecture_name=lecture_name
        self.day=day
        self.slot=slot
    def __str__(self):
        return f"{self.lecture_name} Section on {self.day} at {' , '.join(self.slot)}"