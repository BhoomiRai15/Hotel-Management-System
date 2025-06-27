from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class report:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1260x620+230+220")

        #title
        lbl_title=Label(self.root,text="HOTEL REPORT",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1260,height=50)

        #logo
        img2=Image.open(r"C:\Users\bhoom\OneDrive\Documents\Python Project\images\logohotel.png")
        img2=img2.resize((100,40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="GRAND HOTEL",fg="gold",bg="black",font=("times new roman",16,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=550,height=550)
         
        ltext="""
The Grand Hotel in Delhi epitomizes luxury,elegance, and historical charm. Located in the heart of India’s vibrant capital, it offers guests an unforgettable experience with its exquisite architecture, world-class amenities, and impeccable service. 

Known for its grandeur and sophisticated atmosphere,the Grand Hotel is a favored destination for travelers seeking a blend of classic Indian hospitality and modern comfort.

Established in the early 20th century, the Grand Hotel has a rich history that enhances its appeal. Over the decades, it has hosted numerous dignitaries, celebrities, and royalty, making it a significant landmark in Delhi’s hospitality sector. 

The hotel’s colonial-style façade stands as a testament to the elegance and opulence of a bygone era.The Grand Hotel's prime location in central Delhi provides easy access to the city’s iconic attractions. 

Guests can conveniently visit India Gate, the Red Fort, and Connaught Place, immersing themselves in Delhi's vibrant culture and history. Its central location also ensures excellent connectivity with public transportation, making it ideal for both leisure and business travelers.
"""
        lbl_cust_contact=Label(labelframeleft,text=ltext,font=("arial",13,"bold"),wraplength=530,padx=2,pady=6,fg="gold",bg="black",justify="left")
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        



        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="HOTEL SERVICES OFFERED",font=("times new roman",16,"bold"),fg="gold",bg="black",padx=2,pady=6,)
        Table_Frame.place(x=560,y=50,width=690,height=550)

        ttext="""
Hotel Service:
1. Accommodation: 24/7
2. Room Service: 24/7
3. Restaurant: Breakfast - 7:00 AM - 11:00 AM
                        Lunch - 12:00 PM - 3:00 PM 
                        Dinner - 6:00 PM - 10:00 PM
4. Concierge: 24/7
5. Business Center: 8:00 AM - 8:00 PM
6. Valet Parking: 24/7
7. Airport Shuttle: On request


Recreational Facilities:
1. Swimming Pool: 7:00 AM - 8:00 PM
2. Gym/Fitness Center: 6:00 AM - 10:00 PM
3. Spa: - By appointment, 9:00 AM - 8:00 PM
            - Services: Massages, facials, body treatments

                  
Addiional Services:
1. Laundry: Same-day service available
2. Wi-Fi: Throughout the hotel, complimentary
"""


        lblSearchBy=Label(Table_Frame,font=("arial",13,"bold"),text=ttext,wraplength=530,padx=2,pady=6,fg="gold",bg="black",justify="left")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)




if __name__=="__main__":
    root=Tk()
    obj=report(root)
    root.mainloop()