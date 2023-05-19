from playsound import playsound

class Hewan:
    def bersuara(self):
        print("suara anjing")

class Anjing(Hewan):
    def bersuara(self):
        print("guk...guk...ajig")
file_path = "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Anjing.mp3"

def bersuara(animal):
        animal.bersuara()

hewan = Hewan()
ajig = Anjing()
bersuara(hewan)
bersuara(ajig)
playsound(file_path)


