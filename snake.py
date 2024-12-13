from animall import animal

class snake(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.habitat = habitat 
        
    #method
    def info_snake(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\nhabitat\t\t\t: ", self.habitat)

print()       
cobra = snake("cobra"," daging", "hutan", "bertelur", "hitam", "darat")
print("## SNAKE 1 ##")
cobra.info_snake()

from animall import animal

class snake(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.habitat = habitat 
        
    #method
    def info_snake(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\nhabitat\t\t\t: ", self.habitat)

print()       
sanca = snake("sanca"," daging", "hutan", "bertelur", "hitam", "darat")
print("## SNAKE 2 ##")
sanca.info_snake()

from animall import animal

class snake(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.habitat = habitat 
        
    #method
    def info_snake(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\nhabitat\t\t\t: ", self.habitat)

print()       
piton = snake("piton"," daging", "hutan", "bertelur", "hitam", "darat")
print("## SNAKE 3 ##")
piton.info_snake()