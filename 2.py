class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        
    def update_phone(self, new_phone):
        self.phone_number = new_phone
        
    def show_info(self):
        print("Ism: ", self.name)
        print("Telefon: ", self.phone_number)
        
    
contact = Contact('Malika', '901234567')

contact.update_phone('931112233')
contact.show_info()
