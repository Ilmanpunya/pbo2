import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Komputer import *
class FrmKomputer:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='ID_KOMPUTER:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BILLING:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUS:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_komputer = Entry(mainFrame) 
        self.txtId_komputer.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_komputer.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Combo Box
        self.txtBilling = StringVar()
        Cbo_Billing = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtBilling) 
        Cbo_Billing.grid(row=1, column=1, padx=5, pady=5)
        # Adding Billing combobox drop down list
        Cbo_Billing['values'] = ('Billing01','Billing02','Billing03','Billing04','Billing05')
        Cbo_Billing.current()
        # Combo Box
        self.txtJenis = StringVar()
        Cbo_Jenis = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJenis) 
        Cbo_Jenis.grid(row=2, column=1, padx=5, pady=5)
        # Adding Jenis combobox drop down list
        Cbo_Jenis['values'] = ('Asus01','Asus02','Dell01','Dell02','Acer01','Acer02')
        Cbo_Jenis.current()
        # Combo Box
        self.txtStatus = StringVar()
        Cbo_Status = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtStatus) 
        Cbo_Status.grid(row=3, column=1, padx=5, pady=5)
        # Adding Status combobox drop down list
        Cbo_Status['values'] = ('Tersedia','Digunakan','Rusak')
        Cbo_Status.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('ID','id_komputer','Billing','Jenis','Status')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('ID', text='ID')
        self.tree.column('ID', width="30")
        self.tree.heading('id_komputer', text='ID_KOMPUTER')
        self.tree.column('id_komputer', width="30")
        self.tree.heading('Billing', text='BILLING')
        self.tree.column('Billing', width="30")
        self.tree.heading('Jenis', text='JENIS')
        self.tree.column('Jenis', width="30")
        self.tree.heading('Status', text='STATUS')
        self.tree.column('Status', width="30")
        # set tree position
        self.tree.place(x=0, y=200, width=430)
        
    def onClear(self, event=None):
        self.txtId_komputer.delete(0,END)
        self.txtId_komputer.insert(END,"")
        self.txtBilling.set("")
        self.txtJenis.set("")
        self.txtStatus.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data komputer
        obj = Komputer()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["ID"],d["id_komputer"],d["Billing"],d["Jenis"],d["Status"]))
    def onCari(self, event=None):
        id_komputer = self.txtId_komputer.get()
        obj = Komputer()
        a = obj.get_by_id_komputer(id_komputer)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_komputer = self.txtId_komputer.get()
        obj = Komputer()
        res = obj.get_by_id_komputer(id_komputer)
        self.txtId_komputer.delete(0,END)
        self.txtId_komputer.insert(END,obj.id_komputer)
        self.txtBilling.set(obj.Billing)
        self.txtJenis.set(obj.Jenis)
        self.txtStatus.set(obj.Status)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_komputer = self.txtId_komputer.get()
        Billing = self.txtBilling.get()
        Jenis = self.txtJenis.get()
        Status = self.txtStatus.get()
        # create new Object
        obj = Komputer()
        obj.id_komputer = id_komputer
        obj.Billing = Billing
        obj.Jenis = Jenis
        obj.Status = Status
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_komputer(id_komputer)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_komputer = self.txtId_komputer.get()
        obj = Komputer()
        obj.id_komputer = id_komputer
        if(self.ditemukan==True):
            res = obj.delete_by_id_komputer(id_komputer)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmKomputer(root2, "Aplikasi Data Komputer")
    root2.mainloop()
