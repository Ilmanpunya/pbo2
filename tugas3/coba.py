from playsound import playsound

# define a dictionary with animal names and their sound files
animal_sounds = {
    "lion": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kucing.mp3",
    "elephant": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Anjing.mp3",
    "tiger": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Burung.mp3",
    "dog": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Gajah.mp3",
    "cat": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kambing.mp3",
    "chimpanzee": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Burung kenari.mp3",
    "cow": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Babi.mp3",
    "pig": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Monyet.mp3",
    "duck": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Kuda.mp3",
    "fox": "D:\\LATIHAN PROGRAM\\pa freddy\\PBO2\\PBO Ilman\\pertemuan3\\tugas\\Bebek.mp3"
}

# play the sound of the animal with the given name
def play_animal_sound(animal_name):
    sound_file = animal_sounds.get(animal_name)
    if sound_file:
        playsound(sound_file)
    else:
        print("Sound file not found for animal:", animal_name)

# main program loop
while True:
    # ask the user to input an animal name
    animal_name = input("Enter an animal name (or 'exit' to quit): ")
    if animal_name == "exit":
        break
    else:
        play_animal_sound(animal_name.lower())