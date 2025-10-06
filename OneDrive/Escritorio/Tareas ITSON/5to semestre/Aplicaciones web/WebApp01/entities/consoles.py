class Consoles:
    def __init__(self, name, model, launch, color):
        self.name = name
        self.model = model
        self.launch = launch
        self.color = color

    @classmethod
    def get_consoles(cls):

        consoles = [
            cls("PS2", "Fat", "2000", "Negro"),
            cls("PS2", "Slim", "2004", "Plateado"),
            cls("Xbox 360", "Fat-Elite", "2006", "Negro"),
            cls("Xbox 360", "Slim", "2007", "Negro mate"),
            cls("PS3", "Super Slim", "2012", "Negro"),
            cls("Xbox One", "Fat", "2013", "Negro"),
            cls("PS4", "Slim", "2016", "Negro"),
            cls("Xbox Series S", "Fat-Slim", "2020", "Blanco")
        ]
        
        return consoles
    