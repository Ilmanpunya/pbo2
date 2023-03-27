#ilman nafis al-fariq
#R4
#210511144

class Kota:
    def __init__(self, nama):
        self.nam = nama
class Wisata:
    def nama(self):
        print("pantai pangandaran terletak di: ", self.nama)
class Pantai:
    def tiket(self, dewasa, anak_anak):
        self.dewasa = dewasa
        self.anak_anak = anak_anak
class Indonesia(Kota, Wisata, Pantai):
    def __init__(self, nama):
        super().__init__(nama)
    def info(self):
        self.nama()
        self.tiket(15,10)
