#Ilman Nafis Al-fariq
#210511144
#Kelas D

class Hewan:
    def bersuara(self):
        print("Hewan tersebut bersuara")

class Sapi(Hewan):
    def bersuara(self):
        print("suara sapi")

class Ayam(Hewan):
    def bersuara(self):
        print("suara ayam")

class Jantan(Sapi):
    def bersuara(self):
        print("suara sapi jantan")

class Betina(Ayam):
    def bersuara(self):
        print("ayam betina bersura")


hewan = Hewan()
hewan.bersuara()

sapi = Sapi()
sapi.bersuara()

ayam = Ayam()
ayam.bersuara()

jantan = Jantan()
jantan.bersuara()

betina = Betina()
betina.bersuara()
