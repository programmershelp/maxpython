from tkinter import *

class Application(Frame):
    def helloworld(self):
        print ("Hello world")

    def helloWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "EXIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["bg"]   = "black"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.helloworld

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.helloWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()