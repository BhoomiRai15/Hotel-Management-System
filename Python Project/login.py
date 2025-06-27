from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import time
import datetime
import mysql.connector
from tkinter import messagebox
from hotel import HotelManagementSystem

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\bhoom\OneDrive\Documents\Python Project\images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\bhoom\OneDrive\Documents\Python Project\images\LoginIconAppl.png")
        img1=img1.resize((100,100))
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=40,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=40,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=320,width=120,height=35)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        elif(self.txtuser.get()=="User" and self.txtpass.get()=="abcd"):
            messagebox.showinfo("Success","Welcome to Grand Hotel!!!")
            self.new_window=Toplevel(self.root)
            self.app=HotelManagementSystem(self.new_window)
        else:
            messagebox.showerror("Inavalid","Invalid Username and Password")


        





if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()







       




