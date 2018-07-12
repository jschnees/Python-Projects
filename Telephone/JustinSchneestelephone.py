from tkinter import *
from data  import *


def whichSelected () :
    print("At %s of %d" % (select.curselection(), len(datalist)))
    return int(select.curselection()[0])

def addEntry () :
    datalist.append ([nameVar.get(), phoneVar.get(), emailVar.get(), addyVar.get()])
    setSelect ()

def updateEntry() :
    datalist[whichSelected()] = [nameVar.get(), phoneVar.get(), emailVar.get(), addyVar.get()]
    setSelect ()

def deleteEntry() :
    del datalist[whichSelected()]
    setSelect ()

def loadEntry  () :
    name, phone, email, addy = datalist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)
    emailVar.set(email)
    addyVar.set(addy)
    
def makeWindow () :
    global nameVar, phoneVar, emailVar, addyVar, select
    win = Tk()
    
    win.title("Telephone Database")
    win.geometry("400x200")
    frame1 = Frame(win)
    frame1.pack()
    win.configure(background='#707070')

    
    # Label for Name
    Label(frame1, text="Name: ",background='#C0C0C0', width=6).grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    # Text Box for Name
    name = Entry(frame1, textvariable=nameVar, width=40, background='#C0C0C0').grid(row=0, column=1, sticky=W)

    # Label for Phone Number
    Label(frame1, text="Phone: ",background='#C0C0C0', width=6).grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    # Text Box for Phone Number
    phone= Entry(frame1, textvariable=phoneVar, width=40, background='#C0C0C0').grid(row=1, column=1, sticky=W)

    # Label for Email
    Label(frame1, text="Email: ",background='#C0C0C0', width=6).grid(row=2, column=0, sticky=W)
    emailVar= StringVar()
    # Text Box for Email
    email= Entry(frame1, textvariable=phoneVar, width=40, background='#C0C0C0').grid(row=2, column=1, sticky=W)

    # Label for Address
    Label(frame1, text="Address: ",background='#C0C0C0', width=6).grid(row=3, column=0, sticky=W)
    addyVar= StringVar()
    # Text Box for Address  
    addy= Entry(frame1, textvariable=addyVar, width=40, background='#C0C0C0').grid(row=3, column=1, sticky=W)
    
    # Row of buttons
    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    #b1.grid(row=4, column=1, sticky=W)
    
    b2 = Button(frame2,text="Update",command=updateEntry)
    #b2.grid(row=4, column=2, sticky=W)
    
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    #b3.grid(row=4, column=3, sticky=W)
    
    b4 = Button(frame2,text="Load",command=loadEntry)
    #b4.grid(row=4, column=4, sticky=W)
    
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    # select of names
    frame3 = Frame(win)
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=5, width=40)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,fill=BOTH, expand=4)
    return win

def setSelect () :
    datalist.sort()
    select.delete(0,END)
    for name,phone,email,addy in datalist :
        select.insert (END, name)

win = makeWindow()
setSelect ()
win.mainloop()

