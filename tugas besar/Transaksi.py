import requests
import json
class Transaksi:
    def __init__(self):
        self.__id=None
        self.__id_pelanggan = None
        self.__Billing = None
        self.__waktu = None
        self.__url = "http://localhost/appwarnet/transaksi_api.php"
                    
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
    def Billing(self):
        return self.__Billing
        
    @Billing.setter
    def Billing(self, value):
        self.__Billing = value
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
            self.__id = item['id_transaksi']
            self.__id_pelanggan = item['id_pelanggan']
            self.__Billing = item['Billing']
            self.__waktu = item['waktu']
        return data
    def simpan(self):
        payload = {
            "id_pelanggan":self.__id_pelanggan,
            "Billing":self.__Billing,
            "waktu":self.__waktu
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_pelanggan(self, id_pelanggan):
        url = self.__url+"?id_pelanggan="+id_pelanggan
        payload = {
            "id_pelanggan":self.__id_pelanggan,
            "Billing":self.__Billing,
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
