class sections:
    def __init__(self,section_type,day=[],slot=[]):
        self.section_type=section_type
        self.day=day
        self.slot=slot
    def __str__(self):
        return f"{self.section_type} Section on {self.day} at {' , '.join(self.slot)}"