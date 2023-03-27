#ilman nafis al-fariq
#R4
#210511144

class Mahasiswa:
    def __init__(self, nama,nim):
        self.nama = nama
        self.nim = nim
    def get_info(self):
        print(f"Nama: {self.nama},Nim: {self.nim}")
class Organisasi(Mahasiswa):
    def __init__(self, nama, nim, umur, jabatan):
        super().__init__(nama, nim)
        self.umur = umur
        self.jabatan = jabatan
    def get_info(self):
        super().get_info()
        print(f"Umur: {self.umur}, Jabatan: {self.jabatan}")
class Bupati(Organisasi):
    def __init__(self, nama, nim, umur,jabatan, tujuan):
        super().__init__(nama, nim, umur, jabatan,)
        self.tujuan = tujuan
    def get_info(self):
        super().get_info
        print(f"Tujuan: {self.tujuan}")
