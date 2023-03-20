#Ilman nafis al-fariq
#R4
#210511144
class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
lingkaranA = Lingkaran(10)
print(f"Luas lingkaran: {lingkaranA.luas()}")