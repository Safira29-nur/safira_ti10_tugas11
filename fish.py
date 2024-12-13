from animall import animal

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
        
        #method
    def info_fish(self):
        super().info_animal()
        print("bernapas\t\t: ", self.bernapas, "\nhabitat\t\t\t: ", self.habitat)
        
print()       
fish = fish("hiu","daging", "laut", "melahirkan", "insang", "air laut")
print("## FISH ##")
fish.info_fish()

from animall import animal

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
        
        #method
    def info_fish(self):
        super().info_animal()
        print("bernapas\t\t: ", self.bernapas, "\nhabitat\t\t\t: ", self.habitat)
        
print()       
paus = fish("paus","daging", "laut", "melahirkan", "insang", "air laut")
print("## FISH 2 ##")
paus.info_fish()

from animall import animal

class fish(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
        
        #method
    def info_fish(self):
        super().info_animal()
        print("bernapas\t\t: ", self.bernapas, "\nhabitat\t\t\t: ", self.habitat)
        
print()       
pari = fish("pari","daging", "laut", "bertelur dan melahirkan", "insang", "air laut")
print("## FISH 3 ##")
pari.info_fish()