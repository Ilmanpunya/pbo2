#Ilman nafis al-fariq
#R4
#210511144
class   Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")
mobilA = Mobil("BMW", "Hijau")
mobilA.info() # Output: Mobil Toyota berwarna Hitam