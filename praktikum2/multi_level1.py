#ilman nafis al-fariq
#R4
#210511144

class Karnivora:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def makan(self):
        print("Karnivora itu pemakan daging")
class Harimau(Karnivora):
    def __init__(self,nama, umur, warna):
        super().__init__(nama, umur)
        self.warna = warna
    def eat(self):
        print("Harimau memakan sekor kelinci")
class Harimau_sumatra(Harimau):
    def __init__(self, nama, umur, warna, kategori):
        super().__init__(nama, umur, warna)
        self.kategori = kategori
    def ket(self):
        print("Harimau sumatra hampir punah")

Makan = Harimau_sumatra("mona", 3, "putih", "mamalia")
Makan.makan()
Makan.eat()
Makan.ket()