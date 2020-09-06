# -- coding: utf-8 --
from tkinter import *
from tkinter import messagebox


class main_block:
    def __init__(self, master):
        self.e = Entry(master)
        self.b = Button(master, text ='Convert')
        self.l1 = Label(master, text='Choose base to convert the num to')
        self.l2 = Label(master, text='Enter your num in dec')
        self.lb = Listbox(master,height = 4, selectmode = SINGLE)

        self.e.grid(row=1, column=0, padx=5)
        self.b.grid(row=2, column=0, pady=5)
        self.l1.grid(row=0, column=2)
        self.l2.grid(row=0, column=0)
        self.lb.grid(row=1, column=2)
        for base in [2, 8, 10, 16][::-1]:
            self.lb.insert(0, base)


    def setFunc(self, func):
        self.b['command'] = eval(f'self.{func}')

    
    def convert(self):
        base = self.lb.get(ACTIVE)
        val = self.e.get()
        if val.isdigit():
            val, value = int(val), int(val)
            res=''
            if val == 0:
                self.e.delete(0, END)
                self.e.insert(0, 0)
            else:
                while val:
                    res+=f'{val%base}'
                    val//=base
                self.e.delete(0, END)
                self.e.insert(0, f"{res[::-1] if base != 16 else hex(value)}")
        else:
            if not val == '':
                messagebox.showerror("Error", f'{val} is NaN')
            else:
                messagebox.showerror("Error", 'Enter something, btw')

root = Tk()
root.resizable(False, False)
root.title("Converter")
mainWindow = main_block(root)
mainWindow.setFunc('convert')
root.mainloop()
