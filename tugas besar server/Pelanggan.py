import requests
import json
class Pelanggan:
    def __init__(self):
        self.__id=None
        self.__id_pelanggan = None
        self.__nama = None
        self.__umur = None
        self.__waktu = None
        self.__url = "http://f0833063.xsph.ru/appwarnet/pelanggan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_pelanggan(self):
        return self.__id_pelanggan
        
    @id_pelanggan.setter
    def id_pelanggan(self, value):
        self.__id_pelanggan = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def umur(self):
        return self.__umur
        
    @umur.setter
    def umur(self, value):
        self.__umur = value
    @property
    def waktu(self):
        return self.__waktu
        
    @waktu.setter
    def waktu(self, value):
        self.__waktu = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_pelanggan(self, id_pelanggan):
        url = self.__url+"?id_pelanggan="+id_pelanggan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__id_pelanggan = item['id_pelanggan']
            self.__nama = item['nama']
            self.__umur = item['umur']
            self.__waktu = item['waktu']
        return data
    def simpan(self):
        payload = {
            "id_pelanggan":self.__id_pelanggan,
            "nama":self.__nama,
            "umur":self.__umur,
            "waktu":self.__waktu
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_pelanggan(self, id_pelanggan):
        url = self.__url+"?id_pelanggan="+id_pelanggan
        payload = {
            "id_pelanggan":self.__id_pelanggan,
            "nama":self.__nama,
            "umur":self.__umur,
            "waktu":self.__waktu
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_pelanggan(self,id_pelanggan):
        url = self.__url+"?id_pelanggan="+id_pelanggan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
    def Login(self):
        payload = {
            "username":self.__nama,
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text