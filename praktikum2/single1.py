#ilman nafis al-fariq
#R4
#210511144

class Barang:
    def __init__(self,jenis,merk):
        self.jenis = jenis
        self.merk = merk
    def dijual(self):
        print(self.jenis, "dijual")
class sepatu(Barang):
    def __init__(self,jenis, merk, harga):
        super().__init__(jenis, merk)
        self.harga =harga
    def terjual(self):
        print("terjual dengan harga", self.harga)

sepatuA = sepatu("sepatu","NIKE",5000)
sepatuA.dijual()
sepatuA.terjual()