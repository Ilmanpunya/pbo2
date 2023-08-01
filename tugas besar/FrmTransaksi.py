import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Transaksi import *
class FrmTransaksi:
    
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
        Label(mainFrame, text='ID_PELANGGAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='BILLING:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='WAKTU:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_pelanggan = Entry(mainFrame) 
        self.txtId_pelanggan.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_pelanggan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Combo Box
        self.txtBilling = StringVar()
        Cbo_Billing = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtBilling) 
        Cbo_Billing.grid(row=1, column=1, padx=5, pady=5)
        # Adding Billing combobox drop down list
        Cbo_Billing['values'] = ('Billing01','Billing02','Billing03','Billing04','Billing05')
        Cbo_Billing.current()
        # Combo Box
        self.txtWaktu = StringVar()
        Cbo_waktu = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtWaktu) 
        Cbo_waktu.grid(row=2, column=1, padx=5, pady=5)
        # Adding waktu combobox drop down list
        Cbo_waktu['values'] = ('1 jam','2 jam','3 jam','4 jam','5 jam')
        Cbo_waktu.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_transaksi','id_pelanggan','Billing','waktu')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_transaksi', text='ID_TRANSAKSI')
        self.tree.column('id_transaksi', width="30")
        self.tree.heading('id_pelanggan', text='ID_PELANGGAN')
        self.tree.column('id_pelanggan', width="30")
        self.tree.heading('Billing', text='BILLING')
        self.tree.column('Billing', width="30")
        self.tree.heading('waktu', text='WAKTU')
        self.tree.column('waktu', width="30")
        # set tree position
        self.tree.place(x=0, y=200, width=430)
        
    def onClear(self, event=None):
        self.txtId_pelanggan.delete(0,END)
        self.txtId_pelanggan.insert(END,"")
        self.txtBilling.set("")
        self.txtWaktu.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data transaksi
        obj = Transaksi()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_transaksi"],d["id_pelanggan"],d["Billing"],d["waktu"]))
    def onCari(self, event=None):
        id_pelanggan = self.txtId_pelanggan.get()
        obj = Transaksi()
        a = obj.get_by_id_pelanggan(id_pelanggan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_pelanggan = self.txtId_pelanggan.get()
        obj = Transaksi()
        res = obj.get_by_id_pelanggan(id_pelanggan)
        self.txtId_pelanggan.delete(0,END)
        self.txtId_pelanggan.insert(END,obj.id_pelanggan)
        self.txtBilling.set(obj.Billing)
        self.txtWaktu.set(obj.waktu)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_pelanggan = self.txtId_pelanggan.get()
        Billing = self.txtBilling.get()
        waktu = self.txtWaktu.get()
        # create new Object
        obj = Transaksi()
        obj.id_pelanggan = id_pelanggan
        obj.Billing = Billing
        obj.waktu = waktu
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_id_pelanggan(id_pelanggan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        id_pelanggan = self.txtId_pelanggan.get()
        obj = Transaksi()
        obj.id_pelanggan = id_pelanggan
        if(self.ditemukan==True):
            res = obj.delete_by_id_pelanggan(id_pelanggan)
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
    aplikasi = FrmTransaksi(root2, "Aplikasi Data Transaksi")
    root2.mainloop()
