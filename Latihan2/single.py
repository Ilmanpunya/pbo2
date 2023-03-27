#ilman nafis al-fariq
#R4
#210511144

# Single inheritance
#Contoh 1:
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
        print(self.nama, "bergerak")
class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu
    def bersuara(self):
        print("Meow!")

kucingA = Kucing("Langit", 3, "Anggora")
kucingA.bergerak() # output: Kitty bergerak
kucingA.bersuara() # output: Meow!

#Contoh 2:
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")
class Dosen(Manusia):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim
    def mengajar(self):
        print(f"{self.nama} dengan NIM {self.nim} sedang belajar.")

dosenA = Dosen("ilman", 20, "210511144")
dosenA.berbicara()
dosenA.mengajar()

#Contoh 3:
class Kendaraan:
    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna
    def berkendara(self):
        print("Kendaraan ini sedang berjalan.")
class SepedaMotor(Kendaraan):
    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc
    def belok(self):
        print("Sepeda motor ini sedang belok.")

motorA = SepedaMotor("Sepeda Motor", "yamaha", "hitam", 125)
motorA.berkendara()
motorA.belok()