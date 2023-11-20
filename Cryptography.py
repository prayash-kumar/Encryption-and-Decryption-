import base64
from tkinter import *
from tkinter import messagebox

screen = Tk() # Create a window screen
screen.geometry("420x420") # Windows size increse or decrease
screen.title("Cryptography Tools:") # Screen titale name
screen.configure(bg="black") # Screen color

# Funcation of Encrypitions :)
def encrypt():
    password = code.get()
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryptions")
        screen1.geometry("400x250")
        screen1.configure(bg="black")

        massege = box.get(1.0, END)
        encode_massege = massege.encode("ascii")
        base64_bytes = base64.b64encode(encode_massege)
        encrypt_text = base64_bytes.decode("ascii") 

        Label(screen1, text="Code is Encrypted", font="Arial 12 bold").place(x=135, y=30)

        box1 = Text(screen1, bd=4, font="Arial 12 bold", wrap=WORD)
        box1.place(x=5, y=70, width=410, height=180)
        box1.insert(END, encrypt_text)

    # Error messege Popup :(
    elif(password == ""):
        messagebox.showerror("Error","Please Enter the Secret Key")
    
    elif(password != "1234"):
        messagebox.showerror("Oops","Invalid Secret Key")

# Foncation of Decrypitions :)
def decrypt():
    password = code.get()
    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryptions")
        screen2.geometry("400x250")
        screen2.configure(bg="black")

        massege = box.get(1.0, END)
        encode_massege = massege.encode("ascii")
        base64_bytes = base64.b64decode(encode_massege)
        encrypt_text = base64_bytes.decode("ascii") 

        Label(screen2, text="Code is Decrypted", font="Arial 12 bold").place(x=135, y=30)

        box1 = Text(screen2, bd=4, font="Arial 12 bold", wrap=WORD)
        box1.place(x=5, y=70, width=410, height=180)
        box1.insert(END, encrypt_text)

    # Error messege Popup :(
    elif(password == ""):
        messagebox.showerror("Error","Please Enter the Secret Key")
    
    elif(password != "1234"):
        messagebox.showerror("Oops","Invalid Secret Key")

# Funcations of Reset
def reset():
    box.delete(1.0,END)
    code.set("")

# Create Box design
# Lable means screen ke ander text likhne ke liye
Label(screen,text="Enter the encryption and decryption text ", font="Arial 12 bold").place(x=60,y=5)

#Text means write a text
box = Text(screen, bd=4, font="Arial 12 bold")
box.place(x=5, y=45, width=410, height=110)

# Lable Heading
Label(screen,text="Enter a Secret Key",font="Arial 12 bold").place(x=130,y=180)

# Entry
code = StringVar()
Entry(textvariable=code, bd=4, font="Arial 12 bold", show="*").place(x=110,y=220)

# Button
Button(screen, text="Encrypt", font="Arial 12 bold", bg="red", fg="white", command=encrypt).place(x=15, y=280, width=80)
Button(screen, text="Decrypt", font="Arial 12 bold", bg="blue", fg="white", command=decrypt).place(x=330, y=280, width=80)
Button(screen, text="Reset", font="Arial 12 bold", bg="black", fg="white", command=reset).place(x=148, y=340, width=120)


mainloop()
