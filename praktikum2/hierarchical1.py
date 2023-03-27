#ilman nafis al-fariq
#R4
#210511144

class Transportasi:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
class Darat(Transportasi):
    def __init__(self,name,jenis):
        super().__init__(name)
        self.jenis = jenis
    def get_jenis(self):
        return self.jenis
class Udara(Transportasi):
    def __init__(self,name,maskapai):
        super().__init__(name)
        self.maskapai = maskapai
    def get_maskapai(self):
        return self.maskapai
class kereta(Darat):
    def __init__(self,name,jenis,tujuan):
        super().__init__(name,jenis)
        self.tujuan = tujuan
    def get_tujuan(self):
        return self.tujuan
