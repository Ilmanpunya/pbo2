#Ilman nafis al-fariq
#R4
#210511144
class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")
mahasiswaB = Mahasiswa("Ilman nafis al-fariq", "210511144")
mahasiswaB.info()