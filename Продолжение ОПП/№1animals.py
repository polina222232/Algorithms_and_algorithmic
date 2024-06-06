class Acellularia:
    def __init__(self):
        self.name = "Acellularia"

class Cellularia(Acellularia):
    def __init__(self):
        super().__init__()
        self.name = "Cellularia"

class Prokaryota(Cellularia):
    def __init__(self):
        super().__init__()
        self.name = "Prokaryota"

class Eukaryota(Cellularia):
    def __init__(self):
        super().__init__()
        self.name = "Eukaryota"

class Unicellularia(Eukaryota):
    def __init__(self):
        super().__init__()
        self.name = "Unicellularia"

class Fungi(Eukaryota):
    def __init__(self):
        super().__init__()
        self.name = "Fungi"

class Plantae(Eukaryota):
    def __init__(self):
        super().__init__()
        self.name = "Plantae"

class Animalia(Eukaryota):
    def __init__(self):
        super().__init__()
        self.name = "Animalia"


acellularia = Acellularia()
print(acellularia.name)

cellularia = Cellularia()
print(cellularia.name)

prokaryota = Prokaryota()
print(prokaryota.name)

eukaryota = Eukaryota()
print(eukaryota.name)

unicellularia = Unicellularia()
print(unicellularia.name)

fungi = Fungi()
print(fungi.name)

plantae = Plantae()
print(plantae.name)

animalia = Animalia()
print(animalia.name)
