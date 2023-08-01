import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmTimer import *
from FrmKomputer import *
from FrmPelanggan import *
from FrmPelanggan1 import *
from FrmTransaksi import *
from PIL import Image,ImageTk


class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("900x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
       
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        

        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu)

        gambar = Image.open('C:\\xampp\htdocs\\appwarnet\\billing.png')
        resized = gambar.resize((900,600),Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized)
        label_gambar = tk.Label(image=photo)
        label_gambar.image = photo
        label_gambar.place(x=0, y=0, relheight=1, relwidth=1)
        
        # Menu Awal
        file_menu1.add_command(
            label='personal', command=self.menu_pelanggan
        )
        file_menu1.add_command(
            label='Admin##', command=self.show_login
        )
        file_menu1.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="File", menu=file_menu1
        )
        
        

    def menuAdmin(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        admin_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Admin
        admin_menu.add_command(
            label='Data Pelanggan', command= lambda: self.new_window("Menu Pelanggan", FrmPelanggan)
        )
        admin_menu.add_command(
            label='Data komputer', command= lambda: self.new_window("Menu komputer", FrmKomputer)
        )
        admin_menu.add_command(
            label='Data transaksi', command= lambda: self.new_window("Menu transaksi", FrmTransaksi)
        )
        admin_menu.add_command(
            label='Data timer', command= lambda: self.new_window("Menu timer", FrmTimer)
        )
        
    

        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu Admin", menu=admin_menu
        )
        
    def menuOperator(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        OP_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

        #menu Operator
        OP_menu.add_command(
            label='Data pelanggan', command= lambda: self.new_window("Menu pelanggan", FrmPelanggan)
        )
        OP_menu.add_command(
            label='Data transaksi', command= lambda: self.new_window("Menu transaksi", FrmTransaksi)
        )

        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu OP", menu=OP_menu
        )
        
    def menuTimer(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        timer = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu timer
        timer.add_command(
            label='TIMER ', command= lambda: self.new_window("TIMER", FrmTimer)
        )
        
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="TIMER", menu=timer
        )
       
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("250x200")
        self.my_w_child.configure(bg='light blue')
        self.my_w_child.resizable(0,0)

        # pasang Label
        Label(self.my_w_child, text='Masuk Sebagai ?',bg='light blue',font=('arial bold',10)).place(x='70', y='10')

        Label(self.my_w_child, text='Username:',bg='light blue').place(x='10', y='42') 
        
        Label(self.my_w_child, text="Password:",bg='light blue').place(x='10', y='72') 

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.place(x='80', y='45', w='120') 
        
        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.place(x='80', y='75', w='120')  
        self.txtPassword.config(show='*')
        self.txtPassword.bind("<Return>",self.onLogin) # menambahkan event Enter key
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',activebackground="blue",
            command=self.onLogin)
        self.btnLogin.place(x='85', y='120', w='90')

    def menu_pelanggan(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("350x300")
        self.my_w_child.configure(bg='light blue')

        self.btnLoginPersonal = Button(self.my_w_child, text='Masuk',activebackground="light blue", command= lambda: self.new_window("Menu Pelanggan", FrmPelanggan1))
        self.btnLoginPersonal.place(x='130', y='125', w='90')
        
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        A.username = u
        A.passwd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        #messagebox.showinfo("showinfo", "status:"+status+"message:"+msg) 
        if(status=="success"):
            self.my_w_child.destroy()
            if(msg=="admin"):
                self.menuAdmin()
            elif(msg=="operator"):
                self.menuOperator()
            elif(msg=="timer"):
                self.menuTimer()
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid") 
        
    def onLogout(self):
        self.aturKomponen()
                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(0,0)
    my_str = tk.StringVar()
    aplikasi = Dashboard(root, "Dashboard Billing")
    root.mainloop() 