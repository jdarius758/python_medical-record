from tkinter import *
import tkinter.messagebox
import mysql.connector
import startup
import doctor



def database():
    con = mysql.connector.connect(host='localhost', port='3306', username='root', password='1234', database='medic+gh')
    m = con.cursor()
    m.execute('INSERT INTO patient (first_name,last_name,tel_no,city,postal_code,height,weight,ethnicity,bloodtype,dr_id,insurance_id,access_level,nic_no,birthdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(firstname.get(),lastname.get(),contact.get(),city.get(),postalcode.get(),height.get(),weight.get(),ethnicity.get(),bloodtype.get(),dr_id.get(),insurance_id.get(),access_level.get(),nic_no.get(),birthdate.get()))
    con.commit()
    con.close()
    tkinter.messagebox.showinfo('message'," Saved Info Into Mysql Database File")









screen = Tk()
screen.geometry("1350x950")
screen.title("Medic+ App")



body = Label(bg="white", width = "500", height = "500")
body.pack()
menu = Menu(screen)
screen.config(menu=menu)

photo = PhotoImage(file="medic.png", width = "400", height = "300")
label = Label(screen,image = photo)
label.place(x = 0, y = 0)
photo1 = PhotoImage(file="medic+.png", width = "1000", height = "900")
label_ = Label(screen,image = photo1)
label_.place(x = 400, y = 0)



myLabel = Label(screen, text="Medic+ Patient Record System",font="372", fg = "blue", bg = "white",)
myLabel.place(x = 850, y =0)

myLabel_ = Label(screen, text="Enter New Patient Record ",font="372", fg = "blue", bg = "white",)
myLabel = Label(screen, text="First Name  :", fg = "blue", bg = "white",)
myLabel2 = Label(screen, text="Last Name:", fg = "blue", bg = "white",)
myLabel3 = Label(screen, text="Contact :", fg = "blue", bg = "white",)
myLabel4 = Label(screen, text="City :", fg = "blue", bg = "white",)
myLabel5 = Label(screen, text="Postal Code:", fg = "blue", bg = "white",)
myLabel6 = Label(screen, text="Height:", fg = "blue", bg = "white",)
myLabel7 = Label(screen, text="Weight:", fg = "blue", bg = "white",)
myLabel8 = Label(screen, text="Ethnicity:", fg = "blue", bg = "white",)
myLabel9 = Label(screen, text="Bloodtype :", fg = "blue", bg = "white",)
myLabel10 = Label(screen, text="Dr.ID :", fg = "blue", bg = "white",)
myLabel11 = Label(screen, text="Insurance ID:", fg = "blue", bg = "white",)
myLabel12 = Label(screen, text="Access level:", fg = "blue", bg = "white",)
myLabel13= Label(screen, text="Nic No.", fg = "blue", bg = "white",)
myLabel14 = Label(screen, text="Birthdate", fg = "blue", bg = "white",)

myLabel_.place(x = 500, y = 360)
myLabel.place(x = 410, y = 400)
myLabel2.place(x = 410, y = 430)
myLabel3.place(x = 410, y = 460)
myLabel4.place(x = 410, y = 490)
myLabel5.place(x = 410, y = 520)
myLabel6.place(x = 410, y = 550)
myLabel7.place(x = 410, y = 580)
myLabel8.place(x = 680, y = 400)
myLabel9.place(x = 680, y = 430)
myLabel10.place(x = 680, y = 460)
myLabel11.place(x = 680, y = 490)
myLabel12.place(x = 680, y = 520)
myLabel13.place(x = 680, y = 550)
myLabel14.place(x = 680, y = 580)

firstname = StringVar()
lastname = StringVar()
contact = StringVar()
city = StringVar()
postalcode = StringVar()
height = StringVar()
weight = StringVar()
ethnicity = StringVar()
bloodtype = StringVar()
dr_id = StringVar()
insurance_id = StringVar()
access_level = StringVar()
nic_no = StringVar()
birthdate = StringVar()







entry1 = Entry(screen, textvariable = firstname)
entry2 = Entry(screen, textvariable = lastname)
entry3 = Entry(screen, textvariable = contact)
entry4 = Entry(screen, textvariable = city)
entry5 = Entry(screen, textvariable = postalcode)
entry6 = Entry(screen, textvariable = height)
entry7 = Entry(screen, textvariable = weight)
entry8 = Entry(screen, textvariable = ethnicity)
entry9 = Entry(screen, textvariable = bloodtype)
entry10 = Entry(screen, textvariable = dr_id)
entry11 = Entry(screen, textvariable = insurance_id)
entry12 = Entry(screen, textvariable = access_level)
entry13 = Entry(screen, textvariable = nic_no)
entry14 = Entry(screen, textvariable = birthdate)



entry1.place(x = 490, y = 400, width = "150")
entry2.place(x = 490, y = 430, width = "150")
entry3.place(x = 490, y = 460, width = "150")
entry4.place(x = 490, y = 490, width = "150")
entry5.place(x = 490, y = 520, width = "150")
entry6.place(x = 490, y = 550, width = "150")
entry7.place(x = 490, y = 580, width = "150")
entry8.place(x = 800, y = 400, width = "150")
entry9.place(x = 800, y = 430, width = "150")
entry10.place(x = 800, y = 460, width = "150")
entry11.place(x = 800, y = 490, width = "150")
entry12.place(x = 800, y = 520, width = "150")
entry13.place(x = 800, y = 550, width = "150")
entry14.place(x = 800, y = 580, width = "150")



def treatment():

    screen3 = Tk()
    screen3.geometry("1000x1000")
    screen3.title("Add New Treatment Page")
    body = Label(screen3, bg="white", width="1000", height="1000")
    body.pack()
    myLabel = Label(screen3, text="Enter name of phone :", fg="green", bg="white", )
    myLabel2 = Label(screen3, text="Enter Service provider :", fg="green", bg="white", )
    myLabel3 = Label(screen3, text="Enter Price of Phone :", fg="green", bg="white", )
    myLabel4 = Label(screen3, text="Enter name of brand :", fg="green", bg="white", )
    myLabel5 = Label(screen3, text="Enter name of model :", fg="green", bg="white", )

    myLabel.place(x=150, y=170)
    myLabel2.place(x=150, y=230)
    myLabel3.place(x=150, y=290)
    myLabel4.place(x=150, y=340)
    myLabel5.place(x=150, y=400)

    name = StringVar()
    service = StringVar()
    price = StringVar()
    brand = StringVar()
    model = StringVar()

    entry1 = Entry(screen3, textvariable=name)
    entry2 = Entry(screen3, textvariable=service)
    entry3 = Entry(screen3, textvariable=price)
    entry4 = Entry(screen3, textvariable=brand)
    entry5 = Entry(screen3, textvariable=model)

    entry1.place(x=300, y=170, width="180")
    entry2.place(x=300, y=230, width="180")
    entry3.place(x=300, y=290, width="180")
    entry4.place(x=300, y=340, width="180")
    entry5.place(x=300, y=400, width="180")

    def database1():
        con = mysql.connector.connect(host='localhost', port='3306', username='root', password='1234', database='phone')
        m = con.cursor()
        m.execute( 'INSERT INTO phoneinfo (phone_name,phone_service,phone_price,phone_brand,phone_model) VALUES (%s,%s,%s,%s,%s)',(name.get(), service.get(), price.get(), brand.get(), model.get()))
        con.commit()
        con.close()

    save = Button(screen3, text="Save Info ", command=lambda: [database1()], width="20", height="2")
    save.place(x=300, y=440)

    screen3.mainloop()


save = Button(text = "Save Info ", command=lambda:[database()], width = "50", height = "2",fg = "blue", bg = "white")
save.place(x = 20, y = 400)

exit1 = Button(text = "Treatment Page", command=lambda:[treatment()], width = "50", height = "2",fg = "blue", bg = "white")
exit1.place(x = 20, y = 480)


exit = Button(text = "Exit app ", command= screen.destroy, width = "50", height = "2",fg = "blue", bg = "white")
exit.place(x = 20, y = 560)






screen.mainloop()
