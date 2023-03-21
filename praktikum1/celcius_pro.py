# Ilman nafis al-fariq
# R4
# 210511144
class Celcius:
    @staticmethod
    def to_fahrenheit(celcius):
        return celcius * (9/5) + 32
    @staticmethod
    def to_reamur(celcius):
        return celcius * 4/5
    @staticmethod
    def to_kelvin(celcius):
        return celcius + 273
    

CF = 95
CR = 60
CK = 90
myfahrenheit = Celcius.to_fahrenheit(CF)
myreamur = Celcius.to_reamur(CR)
mykelvin = Celcius.to_kelvin(CK)
print("konversi ", CF, "Derajat celcius",myfahrenheit,"Derajat fahrenheit" )
print("konversi ", CR, "Derajat celcius",myreamur,"Derajat reamur" )
print("konversi ", CK, "Derajat celcius",mykelvin,"Derajat kelvin" )
