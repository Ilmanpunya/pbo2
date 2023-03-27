#ilman nafis al-fariq
#R4
#210511144

class Tumbuhan:
    def __init__(self,nama, fungsi):
        self.nama = nama
        self.fungsi = fungsi
    def fotosintesis(self):
        print(self.nama, "melakukan fotosintesis di pagi hari")
class bunga(Tumbuhan):
    def __init__(self, nama, fungsi, harga):
        super().__init__(nama, fungsi)
        self.harga = harga
    def digunakaan(self):
        print(self.nama, "digunakan untuk pajangan dan dijual dengan harga", self.harga)
    
bungaA = bunga("mawar", "pajangan", 25000)
bungaA.fotosintesis()
bungaA.digunakaan()