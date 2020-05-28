from tkinter import *

class Calculator:

    def __init__(self, master):
        self.master = master

    
        master.title("Calculator")
        master.geometry("400x400")
        master.configure(bg='lightblue')
        
        frame1=Frame(master)
        frame1.pack(side=TOP)

        framea=Frame(master)
        framea.pack(side=TOP)
        
        frame2=Frame(master)
        frame2.pack(side=TOP)

        frameb=Frame(master)
        frameb.pack(side=TOP)
        
        frame3=Frame(master)
        frame3.pack(side=TOP)

        framec=Frame(master)
        framec.pack(side=TOP)
        frame4=Frame(master)
        frame4.pack(side=TOP)
        
        self.label1=Label(frame1, text="Enter the first number:")
        

        
        self.entry1 = Entry(frame1,bd=5)
        
        
        self.total=0
        self.label2=Label(frame2, text="Enter the second number:")
        
        self.entry2 = Entry(frame2,bd=5)
        
        self.total_text = IntVar()
        self.total_text.set(self.total)
        self.t= Label(frame4,text="RESULT = ")
        self.total_label = Label(frame4,textvariable=self.total_text)

        self.labelf1 = Label(frame1 , text="    ", bg='lightblue')
        self.labelf2 = Label(frame2 , text="    ", bg='lightblue')
        self.labelf3 = Label(frame3 , text="    ", bg='lightblue')
        self.labelf4 = Label(frame3 , text="    ", bg='lightblue')
        self.labelf5 = Label(frame3 , text="    ", bg='lightblue')
        self.labelf6 = Label(frame3 , text="    ", bg='lightblue')

        self.labelf7 = Label(framea , text="              ", bg='lightblue')
        self.labelf8 = Label(frameb , text="              ", bg='lightblue')
        self.labelf9 = Label(framec , text="              ", bg='lightblue')
       
       

        self.add_button = Button(frame3, text="Add", command=lambda: self.update("add"))
        self.subtract_button = Button(frame3, text="Subtract", command=lambda: self.update("subtract"))
        self.multiply_button = Button(frame3, text="Multiply", command=lambda: self.update("multiply"))
        self.divide_button = Button(frame3, text="Divide", command=lambda: self.update("divide"))
        

        # LAYOUT
        
        self.label1.pack(side=LEFT)
        self.labelf1.pack(side=LEFT)
        self.entry1.pack(side=LEFT)

        self.labelf7.pack(side=LEFT)
        self.label2.pack(side=LEFT)        
        self.labelf2.pack(side=LEFT)
        self.entry2.pack(side=LEFT)

        self.labelf8.pack(side=LEFT)
        self.add_button.pack(side=LEFT)
        self.labelf3.pack(side=LEFT)
        self.subtract_button.pack(side=LEFT)
        self.labelf4.pack(side=LEFT)
        self.multiply_button.pack(side=LEFT)
        self.labelf5.pack(side=LEFT)
        self.divide_button.pack(side=LEFT)
        self.labelf6.pack(side=LEFT)
        
        self.labelf9.pack(side=LEFT)
        self.t.pack(side=LEFT)
        self.total_label.pack(side=BOTTOM)
        
        
  
