class Ticket:
    def __init__(self, nom, narx, son):
        self.nom = nom
        self.narx = narx
        self.son = son
        
    def total_cost(self):
        return self.son * self.narx
        
    def show_info(self):
        return(self.nom, self.narx, self.son)
        
        
        
ticket = Ticket('Avatar', 40000, 3)

print(ticket.total_cost())
