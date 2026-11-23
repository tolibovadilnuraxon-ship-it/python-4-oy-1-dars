class Athlete:
    def __init__(self, ism, tur, yosh):
        self.ism = ism
        self.tur = tur
        self.yosh = yosh
        
    def show_info(self):
        print("Ism: ", self.ism)
        print("Sport turi:", self.tur)
        print("Yosh: ", self.yosh)
        
    
athlete = Athlete('Ali', 'Futbol', 20)
athlete.show_info()
