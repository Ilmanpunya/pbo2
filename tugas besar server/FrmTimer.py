import tkinter as tk
from tkinter import messagebox,Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar

class FrmTimer:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("300x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW")
        self.ditemukan = None
        self.aturKomponen()
        
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg='light blue')


        self.seconds_left = 7200  # Waktu countdown 2 jam = 7200 detik

        
        self.time_label = Label(mainFrame, font = ("Helvetica", 20), text = "waktu: 00:00:00",bg='blue',fg='white')
        self.time_label.pack(pady=20)
        self.stop_button = Button(mainFrame, font = ("Helvetica", 10), text = "selesai", command = self.stop)
        self.stop_button.pack(pady=20)
        self.update_label()

    def update_label(self):
        hours, remainder = divmod(self.seconds_left, 3600)
        minutes, secs = divmod(remainder, 60)

        self.time_label.config(text=f"waktu: {hours:02d}:{minutes:02d}:{secs:02d}")

        if self.seconds_left > 0:
            self.seconds_left -= 1
            self.parent.after(1000, self.update_label)
        else:
            messagebox.showinfo("Selesai", "waktu telah selesai!")

        
    def stop(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin selesai ?"):
            self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    app = FrmTimer(root2,'timer')
    root2.mainloop()