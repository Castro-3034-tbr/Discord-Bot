class User():
    """Class to save the information of the user"""
    
    def __init__(self, name, id, avatar):
        self.name = name
        self.id = id
        self.avatar = avatar
        self.warnings = 0
        
    def add_warning(self):
        """Function to add a warning to the user"""
        self.warnings += 1
    
    def get_warnings(self):
        """Fuction to return the warnings of the user"""
        return self.warnings
    
    def get_name(self):
        """Fuction to return the name of the user"""
        return self.name
    
    def __str__(self):
        cadena = "Nombre: " + self.name + "id: " + self.id + "avatar: " + self.avatar + "warnings: " + str(self.warnings)
        return cadena
    

