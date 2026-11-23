class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100
        
    def use_energy(self, amount):
        self.energy = max(self.energiya - amount, 0)
        
    def show_status(self):
        print("Ism: ", self.ism)
        print("Energiya: ", self.energy)
        
        
player = Player('Hero')

player.use_energy(35)
player.show_status()
