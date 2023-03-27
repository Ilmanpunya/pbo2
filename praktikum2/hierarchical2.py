#ilman nafis al-fariq
#R4
#210511144

class Karnivora:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def get_nama(self):
        return self.nama
    def get_jenis(self):
        return self.jenis
class Reptil(Karnivora) :
    def __init__(self, nama, jenis, habitat):
        super().__init__(nama, jenis)
        self.habitat = habitat
    def get_habitat(self):
        return self.habitat
class Singa(Karnivora):
    def __init__(self, nama, jenis, warna):
        super().__init__(nama, jenis)
        self.warna = warna
    def get_warna(self):
        return self.warna
class Buaya(Reptil):
    def __init__(self, nama, jenis, habitat, umur):
        super().__init__(nama, jenis, habitat)
        self.umur = umur
    def get_umur(self):
        return self.umur