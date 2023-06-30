from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog
from functools import partial
from PIL import ImageTk, Image

   
global filename
button_height = 2
button_width = 25
    
def browseFiles():
    browseFiles.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",)
    label_file_explorer.configure(text="File Opened: " + browseFiles.filename)

    pass_label.pack()
    password.pack()
    temp_label.pack()
    button_encrypt.pack()
    button_decrypt.pack() 
   

def encrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as file:  original = file.read()
    encrypted = fernet.encrypt(original)

    with open(browseFiles.filename, 'wb') as encrypted_file:    encrypted_file.write(encrypted)

    status_label.configure(text="Encrypted", width=13, height=2, fg="white", bg="#C48793", font =("",27))
    status_label.pack()

def decrypt_file(p_word):
    temp_key = p_word.get()
    temp_key = ''.join(e for e in temp_key if e.isalnum())
    key = temp_key + ("s" * (43 - len(temp_key)) + "=")

    fernet = Fernet(key)

    with open(browseFiles.filename, 'rb') as enc_file:  encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(browseFiles.filename, 'wb') as dec_file:  dec_file.write(decrypted)

    status_label.configure(text="Decrypted", width=13, height=2, fg="black", bg="#C48793", font =("",27))
    status_label.pack()


window = Tk()

window.title('File Explorer')
window.geometry("1234x585")
window.config(background="black")

#define icon
p1 = PhotoImage(file = 'profile_icon.png')
# Icon set for program window
window.iconphoto(False, p1)

#define image
bg = ImageTk.PhotoImage(file="images/py_image.jpg")
my_label=Label(window, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#create a canvas
#my_canvas = Canvas(window, width=940, height=740)
#my_canvas.pack(fill="both", expand=True)
#set image in canvas
#my_canvas.create_image(0,0, image=bg, anchor="nw")
'''def resizer(e):
    global bg1, resized_bg, new_bg
    #open image
    bg1 = Image.open("images/crypto.png")
    #resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    #define our image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    # Add it back to the canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")'''
main_title = Label(window, text="File Encryptor and Decryptor", width=58, height=2, fg="white", bg="#4c96a0",font =("",27))
passwd = StringVar()

submit_para_en = partial(encrypt_file, passwd)
submit_para_de = partial(decrypt_file, passwd)

credit = Label(window,text = "Developed by Devi Purnima",bg="#4c96a0", height=2, width=111, fg = "black", font =("",15))
label_file_explorer = Label(window, text="File Name : ", width=65, height=2, fg="black", bg="#4c96a0",font =("",20))
pass_label = Label(window, text="Password for encryption/decryption : ", width=30, height=2, fg="black", bg="#4c96a0",font =("",17))
temp_label = Label(window, text="", height=3, bg="black")

button_explore = Button(window, text="Browse File", command=browseFiles, width=button_width, height=button_height, font =("",15), bg="#4ca058", activebackground="pink")

password = Entry(window, textvariable=passwd,show="*", bg="#4c96a0",  font =("",19))

button_encrypt = Button(window, text="Encrypt", command=submit_para_en, width=button_width, height=button_height, font =("",15), fg="white", activebackground="#4c96a0", bg="#438D80")
button_decrypt = Button(window, text="Decrypt", command=submit_para_de, width=button_width, height=button_height, font =("",15), fg="white", activebackground="#4c96a0", bg="#7D0552")

status_label = Label(window, text="", width=100, height=4, fg="white", bg="black",font =("",17))

credit.pack()
main_title.pack()
label_file_explorer.pack()
button_explore.pack()

#window.bind('<Configure>', resizer)
window.mainloop()


