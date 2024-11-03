from tkinter import *
from tkinter import messagebox
import qrcode
import os
import webbrowser


class AppGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('QR Code Generator')
        self.geometry('400x200')
        
        self.e1=Entry(width=20)
        self.e1.place(x=150,y=50)
        
        self.e2=Entry(width=20)
        self.e2.place(x=150,y=80)
        
        self.text_label=Label(self,text='input: ').place(x=90,y=50)
        self.name_label=Label(self,text='file name: ').place(x=90,y=80)
        self.button=Button(self,text='submit',command= self.create_qr).place(x=170,y=150)
        self.mainloop()
  

    def create_qr(self,):
        name=self.e2.get()
        text=self.e1.get()
        if not text or not name:
            messagebox.showerror("ERROR","please write s.th")
    
        img=qrcode.make(text)
        
        file_name=f'{name}.jpeg'
        if os.path.exists(file_name):
            overwrite = messagebox.askyesno("Overwrite", f"{file_name} already exists. Overwrite?")
            if not overwrite:
                return
        img.save(f'{name}.jpeg')
        messagebox.showinfo("Success",f"your QR code saved as {file_name} . Opening in 5 seconds...")
        self.after(5000,lambda: webbrowser.open(file_name))
        

if __name__ == '__main__':
    app=AppGUI()