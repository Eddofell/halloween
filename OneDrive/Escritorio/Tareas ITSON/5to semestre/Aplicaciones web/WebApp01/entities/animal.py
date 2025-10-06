
class Animal:
    def __init__(self, species, name, color):
        self.species = species
        self.name = name
        self.color = color
    
    @classmethod
    def get_list(cls):
        
        animals = [
            cls("Perro", "Bombón", "Naranja"),
            cls("Perro", "Canelo", "Café"),
            cls("Perra/Cangura", "Vainilla", "Tricolor"),
            cls("Perrito", "Bimbo", "Blanco"),
            cls("Perico", "Rex", "Verde"),
            cls("Carpincho", "Capiboy", "Café")
                    ]
        return animals

