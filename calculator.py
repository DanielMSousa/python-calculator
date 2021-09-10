from tkinter import *

class Calculadora:
    def __init__(self):
        self.root = Tk()
        self.config_window()
        self.create_buttons()
        self.root.mainloop()
    
    def config_window(self):
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.screen_frame = Frame(self.root, bg='#2c2c2c')
        self.screen_frame.place(relx=0, rely=0, relwidth=1, relheight=0.22)

        #The label that shows the results
        self.equation = ''
        self.eqvar = StringVar()
        self.eqvar.set(self.equation)

        self.resultLabel = Label(self.screen_frame, textvariable=self.eqvar,
            bg='#2c2c2c', fg='#ffffff', font=(None, 18), anchor="e")
        self.resultLabel.pack(side = RIGHT, padx=20, pady=(30, 0))

        self.button_frame = Frame(self.root)
        self.button_frame.place(relx=0.001, rely=0.23, relwidth=0.999, relheight=0.77)

    def create_buttons(self):
        # Row 1
        self.ac = Button(self.button_frame, text='C', command=self.clean)
        self.ac.place(relx=0, rely=0, relwidth=0.75, relheight=0.2)

        self.bdivision = Button(self.button_frame, text='/', command=lambda: self.put_symbol('/'))
        self.bdivision.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.2)

        # Row 2
        self.b7 = Button(self.button_frame, text='7', command=lambda: self.put_symbol('7'))
        self.b7.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)
        
        self.b8 = Button(self.button_frame, text='8', command=lambda: self.put_symbol('8'))
        self.b8.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)

        self.b9 = Button(self.button_frame, text='9', command=lambda: self.put_symbol('9'))
        self.b9.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)

        self.bmulti = Button(self.button_frame, text='*', command=lambda: self.put_symbol('*'))
        self.bmulti.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)

        # Row 3
        self.b4 = Button(self.button_frame, text='4', command=lambda: self.put_symbol('4'))
        self.b4.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)
        
        self.b5 = Button(self.button_frame, text='5', command=lambda: self.put_symbol('5'))
        self.b5.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)

        self.b6 = Button(self.button_frame, text='6', command=lambda: self.put_symbol('6'))
        self.b6.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)

        self.bsub = Button(self.button_frame, text='-', command=lambda: self.put_symbol('-'))
        self.bsub.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)

        #Row 4
        self.b1 = Button(self.button_frame, text='1', command=lambda: self.put_symbol('1'))
        self.b1.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)
        
        self.b2 = Button(self.button_frame, text='2', command=lambda: self.put_symbol('2'))
        self.b2.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)

        self.b3 = Button(self.button_frame, text='3', command=lambda: self.put_symbol('3'))
        self.b3.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)

        self.bplus = Button(self.button_frame, text='+', command=lambda: self.put_symbol('+'))
        self.bplus.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)

        #Row 5 - last one
        self.b0 = Button(self.button_frame, text='0', command=lambda: self.put_symbol('0'))
        self.b0.place(relx=0, rely=0.8, relwidth=0.5, relheight=0.2)

        self.bdot = Button(self.button_frame, text='.', command=self.put_dot)
        self.bdot.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)

        self.bequal = Button(self.button_frame, text='=', command=self.equal)
        self.bequal.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    def put_symbol(self, symbol):
        self.equation = self.equation + symbol
        self.eqvar.set(self.equation)

    def put_dot(self):
        print('I need to check if the dot already exists')

    def clean(self):
        self.equation = ''
        self.eqvar.set(self.equation)
    
    def equal(self):
        if(self.equation == ''):
            self.equation = '0'
        
        else:
            self.equation = str(eval(self.equation))
        
        self.eqvar.set(self.equation)


Calculadora()