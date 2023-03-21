#Ilman nafis al-fariq
#R4
#210511144
class Celcius:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return 9/5 * (self.celcius) + 32
    def to_reamur(self):
        return (self.celcius) * 4/5
    def to_kelvin(self):
        return (self.celcius) + 273
    
CF = 95
CR = 60
CK = 90
myfahrenheit = Celcius(95)
myreamur = Celcius(60)
mykelvin = Celcius(90)
print("konversi", CF,f"derajat celcius adalah {myfahrenheit.to_fahrenheit()} derajat fahrenheit")
print("konversi", CR,f"derajat celcius adalah {myreamur.to_reamur()} derajat reamur")
print("konversi", CK,f"derajat celcius adalah {mykelvin.to_kelvin()} derajat kelvin")
