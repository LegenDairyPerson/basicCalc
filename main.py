import tkinter as tk
root = tk.Tk()


class app(tk.Frame):

    # called on class call (loops constantly)
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.answertext = "answer will appear here!"
        self.create_widgets()
        self.prev_val = 0
        self.operator = "+"

    # functions called on clicking of respective buttons
    # when 0 clicked
    def click0(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '0'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}0'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 1 clicked
    def click1(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '1'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}1'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 2 clicked
    def click2(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '2'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}2'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 3 clicked
    def click3(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '3'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}3'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 4 clicked
    def click4(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '4'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}4'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 5 clicked
    def click5(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '5'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}5'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 6 clicked
    def click6(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '6'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}6'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 7 clicked
    def click7(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '7'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}7'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 8 clicked
    def click8(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '8'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}8'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when 9 clicked
    def click9(self):
        if self.answertext == "answer will appear here!":
            self.answertext = '9'
        elif self.answertext != "answer will appear here!":
            self.answertext = f'{self.answertext}9'
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")

    # when + clicked
    def clickAdd(self):
        self.prev_val = self.answertext
        self.operator = "+"
        if self.answertext == "answer will appear here!":
            pass
        elif self.answertext != "answer will appear here!":
            self.answertext = '+'
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # when - clicked
    def clickSub(self):
        self.prev_val = self.answertext
        self.operator = "-"
        if self.answertext == "answer will appear here!":
            pass
        elif self.answertext != "answer will appear here!":
            self.answertext = '-'
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # when / clicked
    def clickDiv(self):
        self.prev_val = self.answertext
        self.operator = "/"
        if self.answertext == "answer will appear here!":
            pass
        elif self.answertext != "answer will appear here!":
            self.answertext = '/'
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # when * clicked
    def clickMul(self):
        self.prev_val = self.answertext
        self.operator = "*"
        if self.answertext == "answer will appear here!":
            pass
        elif self.answertext != "answer will appear here!":
            self.answertext = '*'
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # when C clicked
    def clickC(self):
        self.prev_val = 0
        self.answertext = 'answer will appear here!'
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # When period clicked
    def clickPE(self):
        self.operator = "*"
        if self.answertext == "answer will appear here!":
            self.answertext = "0."
        elif self.answertext != "answer will appear here!":
            self.answertext = f"{self.answertext}."
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # when = clicked
    def clickequal(self):
        if self.operator == "+":
            self.answertext = f"{float(self.prev_val) + float(self.answertext[1:])}"
        elif self.operator == "-":
            self.answertext = f"{float(self.prev_val) - float(self.answertext[1:])}"
        elif self.operator == "/":
            self.answertext = f"{float(self.prev_val) / float(self.answertext[1:])}"
        elif self.operator == "*":
            self.answertext = f"{float(self.prev_val) * float(self.answertext[1:])}"
        self.answer = tk.Message(self, text = f'{self.answertext}', bd = 1, relief = "solid", padx = 0, pady = 50)
        self.answer.grid(row = 0, column = 0, columnspan = 4, sticky = "ew")

    # Button creation
    def create_widgets(self):
        self.answer = tk.Message(self, text=f'{self.answertext}', bd=1, relief="solid", padx=0, pady=50)
        self.ce = tk.Button(self, text="C", padx=50, pady=50, command = self.clickC)
        self.dec = tk.Button(self, text=".", padx=50, pady=50, command = self.clickPE)
        self.num1 = tk.Button(self, text="1", padx=50, pady=50, command=self.click1)
        self.num2 = tk.Button(self, text="2", padx=50, pady=50, command=self.click2)
        self.num3 = tk.Button(self, text="3", padx=50, pady=50, command=self.click3)
        self.num4 = tk.Button(self, text="4", padx=50, pady=50, command=self.click4)
        self.num5 = tk.Button(self, text="5", padx=50, pady=50, command=self.click5)
        self.num6 = tk.Button(self, text="6", padx=50, pady=50, command=self.click6)
        self.num7 = tk.Button(self, text="7", padx=50, pady=50, command=self.click7)
        self.num8 = tk.Button(self, text="8", padx=50, pady=50, command=self.click8)
        self.num9 = tk.Button(self, text="9", padx=50, pady=50, command=self.click9)
        self.num0 = tk.Button(self, text="0", padx=50, pady=50, command=self.click0)
        self.add = tk.Button(self, text="+", padx=50, pady=50, command=self.clickAdd)
        self.sub = tk.Button(self, text="-", padx=50, pady=50, command=self.clickSub)
        self.div = tk.Button(self, text="/", padx=50, pady=50, command=self.clickDiv)
        self.mul = tk.Button(self, text="*", padx=50, pady=50, command=self.clickMul)
        self.eq = tk.Button(self, text="=", padx=50, pady=50, command=self.clickequal)
        self.answer.grid(row=0, column=0, columnspan=4, sticky="ew")
        self.ce.grid(row=1, column=0)
        self.dec.grid(row=5, column=2, sticky="ew")
        self.num1.grid(row=4, column=0)
        self.num2.grid(row=4, column=1)
        self.num3.grid(row=4, column=2)
        self.num4.grid(row=3, column=0)
        self.num5.grid(row=3, column=1)
        self.num6.grid(row=3, column=2)
        self.num7.grid(row=2, column=0)
        self.num8.grid(row=2, column=1)
        self.num9.grid(row=2, column=2)
        self.num0.grid(row=5, column=0, columnspan=2, sticky="ew")
        self.add.grid(row=2, column=3, rowspan=2, sticky="ns")
        self.sub.grid(row=1, column=3)
        self.div.grid(row=1, column=1)
        self.mul.grid(row=1, column=2)
        self.eq.grid(row=4, column=3, rowspan=2, sticky="ns")


app = app(master=root)
app.mainloop()
