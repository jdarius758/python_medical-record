from tkinter import *
import mysql.connector
import tkinter.messagebox






def database():
    con = mysql.connector.connect(host='localhost', port='3306', username='root', password='1234', database='medic+gh')
    m = con.cursor()
    m.execute('INSERT INTO doctorlog (firstname,lastname,dep_id,contact_no) VALUES (%s,%s,%s,%s)',(firstname.get(),lastname.get(),department.get(),contact.get()))
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

myLabel_ = Label(screen, text="Enter Doctor's Record ",font="372", fg = "blue", bg = "white",)
myLabel = Label(screen, text="First Name  :", fg = "blue", bg = "white",)
myLabel2 = Label(screen, text="Last Name:", fg = "blue", bg = "white",)
myLabel3 = Label(screen, text="Departent :", fg = "blue", bg = "white",)
myLabel4 = Label(screen, text="Contact:", fg = "blue", bg = "white",)

myLabel.place(x = 410, y = 400)
myLabel2.place(x = 410, y = 430)
myLabel3.place(x = 410, y = 460)
myLabel4.place(x = 410, y = 490)

firstname = StringVar()
lastname = StringVar()
department = StringVar()
contact = StringVar()



entry1 = Entry(screen, textvariable = firstname)
entry2 = Entry(screen, textvariable = lastname)
entry3 = Entry(screen, textvariable = department)
entry4 = Entry(screen, textvariable = contact)

entry1.place(x = 490, y = 400, width = "150")
entry2.place(x = 490, y = 430, width = "150")
entry3.place(x = 490, y = 460, width = "150")
entry4.place(x = 490, y = 490, width = "150")

save = Button(text = "Save Info ", command=lambda:[database()], width = "50", height = "2",fg = "blue", bg = "white")
save.place(x = 20, y = 400)
save = Button(text = "Add patient Information ", command=screen.destroy, width = "50", height = "2",fg = "blue", bg = "white")
save.place(x = 20, y = 480)

screen.mainloop()
