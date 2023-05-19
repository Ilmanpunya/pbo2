# Ilman Nafis Al-fariq
# 210511144
# Kelas D

from playsound import playsound

print("=" * 40)
print("list suara hewan : kucing, anjing, burung, gajah, kambing, burung kenari, babi, monyet, kuda dan bebek ")
print("=" * 40)
suara_hewan = {
    "kucing": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kucing.mp3",
    "anjing": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Anjing.mp3",
    "burung": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Burung.mp3",
    "gajah": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Gajah.mp3",
    "kambing": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kambing.mp3",
    "burung kenari": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Burung kenari.mp3",
    "babi": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Babi.mp3",
    "monyet": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Monyet.mp3",
    "kuda": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kuda.mp3",
    "bebek": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Bebek.mp3"
}

def bersuara(nama_hewan):
    file_sound = suara_hewan.get(nama_hewan)
    if file_sound:
        playsound(file_sound)
    else:
        print("suara hewan tidak di temukan:", suara_hewan)

while True:

    nama_hewan = input("Masukan nama hewan yang ingin didengar = ")
    if nama_hewan == "exit":
        break
    else:
        bersuara(nama_hewan.lower())
