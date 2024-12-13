from animall import animal

class bird(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    #method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\njenis paruh\t\t: ", self.paruh)

print()       
bird = bird("elang"," daging", "tebing", "bertelur", "coklat", "bengkok&lancip")
print("## BIRD ##")
bird.info_bird()

from animall import animal

class bird(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    #method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\njenis paruh\t\t: ", self.paruh)

print()       
kakatua = bird("kakatua"," biji-bijian", "hutan", "bertelur", "merah", "bengkok")
print("## BIRD 2 ##")
kakatua.info_bird()

from animall import animal

class bird(animal):
    #kontruktur property
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    #method
    def info_bird(self):
        super().info_animal()
        print("warna\t\t\t: ", self.warna, "\njenis paruh\t\t: ", self.paruh)

print()       
cendrawasih = bird("cendrawasih"," biji-bijian dan buah", "hutan", "bertelur", "coklat kuning", "lancip")
print("## BIRD 3 ##")
cendrawasih.info_bird()