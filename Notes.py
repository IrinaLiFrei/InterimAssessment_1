#from datetime import datetime

class Notes:
    #now = datetime.now()
    def __init__(self, title, text, time):
        self.title = title
        self.text = text
        self.time = time

    def get_title(self):
        return self.title

    def get_time(self):
        return self.time
    
    def get_text(self):
        return self.text
    



