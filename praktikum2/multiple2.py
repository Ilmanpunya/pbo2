#ilman nafis al-fariq
#R4
#210511144

class Kendaraan:
    def __init__(self,jenis,merk):
        self.jenis = jenis
        self.merk = merk
    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Merk: {self.merk}")
class Umum:
    def __init__(self, kategori, kapasitas):
        self.kategori = kategori
        self.kapasitas = kapasitas
    def display_info(self):
        print(f"Kategori: {self.kategori}")
        print(f"Kapasitas: {self.kapasitas}")
class Mobil:
    def __init__(self, warna, Hsp):
        self.warna = warna
        self.Hsp = Hsp
    def display_info(self):
        print(f"Warna: {self.warna}")
        print(f"Hsp: {self.Hsp}")
class Buss(Umum, Mobil):
    def __init__(self,jenis,merk,kategori,kapasitas,warna,Hsp):
        Kendaraan.__init__(self,jenis,merk)
        Umum.__init__(self,kategori,kapasitas)
        Mobil.__init__(self,warna,Hsp)
    def display_info(self):
        super().display_info()
        print(f"Jenis: {self.jenis}")
        print(f"Merk: {self.merk}")
        print(f"Kategori: {self.kategori}")
        print(f"Kapasitas: {self.kapasitas}")
        print(f"Warna: {self.warna}")
        print(f"Hsp: {self.Hsp}")
busA = Buss("besar", "Honda","angkutan umum",50, "merah", 1000)
busA.display_info()