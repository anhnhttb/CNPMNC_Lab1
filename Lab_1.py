from tkinter import *
from tkinter import messagebox
def btnShowclick():
	name: lbName.get()
	messagebox.showinfo("thông báo", e1.get())
frm = Tk()
frm.title("Lập trình tkinter")
lbName= Label(frm,text ="Nhap ten:").grid(row = 0)
e1 = Entry(frm)
e1.grid(row=0,column=1)
#lbName.pack()
btnShow=Button(frm, text="Xuất",bg="cyan", fg="red", command=btnShowclick)
btnShow.grid(column=1,row=1)
frm.mainloop()
