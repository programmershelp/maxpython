import randfacts

def get_fact():
    txt1.config(state='normal')
    txt1.delete('1.0', tk.END)
    myfact = randfacts.getFact(False)
    txt1.insert(tk.END,myfact)
    txt1.config(state='disabled')
     
def exit():
    window.destroy()
 
import tkinter as tk
window = tk.Tk()
window.geometry("700x250")
window.config(bg="blue")
window.resizable(width=False,height=False)
window.title('FACT APP')
 
lbl1 = tk.Label(window,text="Welcome to the Fact App",font=("Arial", 25),fg="Black",bg="yellow")
lbl2= tk.Label(window,text="Click on the 'Get A Fact!' button to get a fact!",font=("Arial", 15,"bold"),fg="Black",bg="yellow")
btn1 = tk.Button(window,text="Get A Fact",font=("Arial", 15),command=get_fact)
btn2 = tk.Button(window,text="Exit",font=("Arial", 15),command=exit)
txt1 = tk.Text(window,width=60,height=4,font=("Arial",15),state='disabled',bg="yellow")
 
lbl1.pack()
lbl2.pack()
btn1.pack()
txt1.pack()
btn2.pack()
 
window.mainloop()