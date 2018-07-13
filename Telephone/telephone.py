from tkinter import *
from data  import *


def whichSelected () :
    """current selection of data"""
    print("At %s of %d" % (select.curselection(), len(datalist)))
    return int(select.curselection()[0])

def addEntry () :
    """ adds data to the datalist file """
    datalist.append ([nameVar.get(), phoneVar.get(), emailVar.get(), addyVar.get(), noteVar.get()])
    setSelect ()

def updateEntry() :
    """ updates data to the datalist file """    
    datalist[whichSelected()] = [nameVar.get(), phoneVar.get(), emailVar.get(), addyVar.get(), noteVar.get()]
    setSelect ()

def deleteEntry() :
    """ deletes a selected data entry from datalist file """
    del datalist[whichSelected()]
    setSelect ()

def loadEntry  () :
    """ loads selected data from the datalist file """
    name, phone, email, addy, note = datalist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)
    emailVar.set(email)
    addyVar.set(addy)
    noteVar.set(note)
    
def makeWindow () :
    """ elements of the program window
    nameVar - contact name
    phoneVar - contact phone number
    emailVar - contact email
    addyVar - contact address
    noteVar - contact notes
    select - holding variable
    btnClr - button colors
    bgClr - background color for window
    fgClr - font color
    entClr - entry text box color

    """
    global nameVar, phoneVar, emailVar, addyVar, noteVar, select
    # global colors of widgets
    btnClr = '#638BB3'
    bgClr = '#708090'
    fgClr = '#ffffff'
    entClr = '#939393'
    
    win = Tk()
    
    win.title("Telephone Database") # program title
    win.geometry("400x300") # sets size of window
    frame1 = Frame(win) # configures frame one
    frame1.pack()
    win.configure(bg=bgClr) # configure the bg color of the window
    frame1.configure(bg=bgClr,pady=10) # configure the bg color and padding of entry frame

    # Label for Name
    Label(frame1, text="Name: ",bg=bgClr, fg=fgClr, width=6).grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    # Text Box for Name
    name = Entry(frame1, textvariable=nameVar, width=40, bg=entClr, relief='flat').grid(row=0, column=1, sticky=W)

    # Label for Phone Number
    Label(frame1, text="Phone: ",bg=bgClr, fg=fgClr, width=6).grid(row=1, column=0, sticky=W)
    phoneVar= StringVar()
    # Text Box for Phone Number
    phone= Entry(frame1, textvariable=phoneVar, width=40, bg=entClr, relief='flat').grid(row=1, column=1, sticky=W)

    # Label for Email
    Label(frame1, text="Email: ",bg=bgClr, fg=fgClr, width=6).grid(row=2, column=0, sticky=W)
    emailVar= StringVar()
    # Text Box for Email
    email= Entry(frame1, textvariable=emailVar, width=40, bg=entClr, relief='flat').grid(row=2, column=1, sticky=W)

    # Label for Address
    Label(frame1, text="Address: ",bg=bgClr, fg=fgClr, width=6).grid(row=3, column=0, sticky=W)
    addyVar= StringVar()
    # Text Box for Address  
    addy= Entry(frame1, textvariable=addyVar, width=40, bg=entClr, relief='flat').grid(row=3, column=1, sticky=W)
 
    # Label for Notes
    Label(frame1, text="Notes: ",bg=bgClr, fg=fgClr, width=6).grid(row=4, column=0, sticky=W)
    noteVar= StringVar()
    # Text Box for Notes
    note= Entry(frame1, textvariable=noteVar, width=40, bg=entClr, relief='flat').grid(row=4, column=1, sticky=W)
    
    # Row of buttons
    frame2 = Frame(win)
    frame2.pack()
    frame2.configure(bg=bgClr,pady=10)

    b1 = Button(frame2,text=" Add  ",command=addEntry, bg=btnClr, activebackground='yellow')

    b2 = Button(frame2,text="Update",command=updateEntry, bg=btnClr, activebackground='yellow')

    b3 = Button(frame2,text="Delete",command=deleteEntry, bg=btnClr, activebackground='yellow')
 
    b4 = Button(frame2,text="Load",command=loadEntry, bg=btnClr, activebackground='yellow')

    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    # select of names
    frame3 = Frame(win)
    frame3.pack(pady=10)
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6, width=50, bg='#708080',selectbackground="#e76e3c", relief='flat')
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,fill=BOTH, expand=4)
    return win

def setSelect () :
    datalist.sort()
    select.delete(0,END)
    for name,phone,email,addy,note in datalist :
        select.insert (END, name + " " + phone)

win = makeWindow()
setSelect ()
win.mainloop()
