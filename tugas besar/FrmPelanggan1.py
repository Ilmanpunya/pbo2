import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pelanggan import *
from FrmTimer import *
class FrmPelanggan1:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
       

    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        Label(mainFrame, text='ID_PELANGGAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='UMUR:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='WAKTU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtId_pelanggan = Entry(mainFrame) 
        self.txtId_pelanggan.grid(row=0, column=1, padx=5, pady=5)
        self.txtId_pelanggan.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtUmur = Entry(mainFrame) 
        self.txtUmur.grid(row=2, column=1, padx=5, pady=5)
        # Combo Box
        self.txtWaktu = StringVar()
        Cbo_waktu = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtWaktu) 
        Cbo_waktu.grid(row=3, column=1, padx=5, pady=5)
        # Adding waktu combobox drop down list
        Cbo_waktu['values'] = ('1 jam','2 jam','3 jam','4 jam','5 jam')
        Cbo_waktu.current()
        
    def onClear(self, event=None):
        self.txtId_pelanggan.delete(0,END)
        self.txtId_pelanggan.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtUmur.delete(0,END)
        self.txtUmur.insert(END,"")
        self.txtWaktu.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    
    def onCari(self, event=None):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        id_pelanggan = self.txtId_pelanggan.get()
        obj = Pelanggan()
        a = obj.get_by_id_pelanggan(id_pelanggan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
            self.btnLoginPersonal = Button(mainFrame, text='Masuk',activebackground="light blue",width=10,bg='red', command= lambda: self.new_window("TIMER", FrmTimer))
            self.btnLoginPersonal.place(x='150', y='10', w='90')
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        id_pelanggan = self.txtId_pelanggan.get()
        obj = Pelanggan()
        res = obj.get_by_id_pelanggan(id_pelanggan)
        self.txtId_pelanggan.delete(0,END)
        self.txtId_pelanggan.insert(END,obj.id_pelanggan)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtUmur.delete(0,END)
        self.txtUmur.insert(END,obj.umur)
        self.txtWaktu.set(obj.waktu)
        # self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        id_pelanggan = self.txtId_pelanggan.get()
        nama = self.txtNama.get()
        umur = self.txtUmur.get()
        waktu = self.txtWaktu.get()
        # create new Object
        obj = Pelanggan()
        obj.id_pelanggan = id_pelanggan
        obj.nama = nama
        obj.umur = umur
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
        obj = Pelanggan()
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
    aplikasi = FrmPelanggan1(root2, "Aplikasi Data Pelanggan")
    root2.mainloop()
