from tkinter import *

screen = Tk()
screen.geometry("997x579")
screen.title("startup")
body = Label(screen, bg="white", width = "1100", height = "1100")
body.pack()

photo1 = PhotoImage(file="start.png", width = "1100", height = "800")
label_ = Label(screen,image = photo1)
label_.place(x = 0, y = 0)
photo2 = PhotoImage(file="doc_profile.png", width = "203", height = "180")
label1 = Label(screen,image = photo2)
label1.place(x = 710, y = 100)


exit = Button(text = "Enter Medic+ Dashboard ", command= screen.destroy, width = "40", height = "2",fg = "blue", bg = "white")
exit.place(x = 680, y = 360)



screen.mainloop()
