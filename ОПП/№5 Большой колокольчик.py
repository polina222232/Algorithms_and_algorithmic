class BigBell:
    def __init__(self):
        self.ring = "ding"  

    def sound(self):
        print(self.ring)
        
        self.ring = "dong" if self.ring == "ding" else "ding"

bell = BigBell()
bell.sound()  
bell.sound() 
bell.sound()  
bell.sound()  