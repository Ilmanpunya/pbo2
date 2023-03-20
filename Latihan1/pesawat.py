#Ilman nafis al-fariq
#R4
#210511144
class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")
pesawatA = PesawatTerbang("Lion air (Private jet)", "Cirebon - Yogyakarta")
pesawatA.info()