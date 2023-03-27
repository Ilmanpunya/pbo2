##ilman nafis al-fariq
#R4
#210511144

class Hewan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna
    def get_info(self):
        print("Nama: ", self.nama)
        print("Warna: ", self.warna)
class Mamalia(Hewan):
    def __init__(self, nama, warna, metamorfosis):
        super().__init__(nama, warna)
        self.metamorfosis = metamorfosis
    def get_info(self):
        print("berkembang biak dengan cara: ", self.metamorfosis)
class Anjing(Hewan):
    def __init__(self, nama, warna, umur, habitat):
        super().__init__(nama, warna)
        self.umur = umur
        self.habitat = habitat
    def get_info(self):
        print("memiliki habitat di: ", self.habitat)
class Bulldog(Mamalia, Anjing):
    def __init__(self, nama, warna, metamorfosis, umur, habitat, jenis):
        Mamalia.__init__(self, nama, warna, metamorfosis)
        Anjing.__init__(self, nama, warna, umur, habitat)
        self.jenis = jenis
    def display_info(self):
        super().get_info()
        print("nama: ", self.nama)
        print("warna: ", self.warna)
        print("Metamorfosis: ", self.metamorfosis)
        print("umur: ", self.umur)
        print("habitat: ", self.habitat)
        print("jenis: ", self.jenis)