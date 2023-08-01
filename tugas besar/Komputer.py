import requests
import json
class Komputer:
    def __init__(self):
        self.__id=None
        self.__id_komputer = None
        self.__Billing = None
        self.__Jenis = None
        self.__Status = None
        self.__url = "http://localhost/appwarnet/komputer_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def id_komputer(self):
        return self.__id_komputer
        
    @id_komputer.setter
    def id_komputer(self, value):
        self.__id_komputer = value
    @property
    def Billing(self):
        return self.__Billing
        
    @Billing.setter
    def Billing(self, value):
        self.__Billing = value
    @property
    def Jenis(self):
        return self.__Jenis
        
    @Jenis.setter
    def Jenis(self, value):
        self.__Jenis = value
    @property
    def Status(self):
        return self.__Status
        
    @Status.setter
    def Status(self, value):
        self.__Status = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_id_komputer(self, id_komputer):
        url = self.__url+"?id_komputer="+id_komputer
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['ID']
            self.__id_komputer = item['id_komputer']
            self.__Billing = item['Billing']
            self.__Jenis = item['Jenis']
            self.__Status = item['Status']
        return data
    def simpan(self):
        payload = {
            "id_komputer":self.__id_komputer,
            "Billing":self.__Billing,
            "Jenis":self.__Jenis,
            "Status":self.__Status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_id_komputer(self, id_komputer):
        url = self.__url+"?id_komputer="+id_komputer
        payload = {
            "id_komputer":self.__id_komputer,
            "Billing":self.__Billing,
            "Jenis":self.__Jenis,
            "Status":self.__Status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_id_komputer(self,id_komputer):
        url = self.__url+"?id_komputer="+id_komputer
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
