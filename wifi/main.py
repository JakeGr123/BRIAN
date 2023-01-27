from tkinter import * 
from tkinter import scrolledtext
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
def open_Toplevel1():
    top1 = Toplevel()
    top1.geometry('450x500')
    top1.config(bg='black')
    thank=Label(top1, text='      The Motherland appreciates   \n your submission',bg='red',fg="yellow", font=('Times New Roman', 25))
    lerud=Button(top1,  text='Leave',bg='red',fg="yellow", font=('Times New Roman', 15), command=root.destroy)

    #load2 = Image.open('lerud image here')
   # resize2 = load2.resize((50, 80), Image.Resampling.LANCZOS)
    #render2 = ImageTk.PhotoImage(resize2)
    #img12 = Label(top1, image=render2)
    #img12.place(x=0, y=0)

    lerud.place(x=200, y=400)
    thank.place(x=5, y=10)


    p2 = PhotoImage(file = 'not.png')
  
# Setting icon of master window
    top1.iconphoto(False, p2)

    top1.mainloop()

root=Tk()
root.geometry('450x500')
root.config(bg='black')
root.title("Property of U.S.S.R.")
  
p1 = PhotoImage(file = 'not.png')
  
# Setting icon of master window
root.iconphoto(False, p1)

# Title Label
ttk.Label(root, 
          text = "Gulag Volunteer Form",
          font = ("Times New Roman", 25), 
          background = 'red', 
          foreground = "yellow").grid(column = 0,
                                     row = 0)
  
# Creating scrolled text 
# area widget
text_area = scrolledtext.ScrolledText(root, 
                                      wrap = tk.WORD, 
                                      width = 40, 
                                      height = 10, 
                                      font = ("Times New Roman",
                                              15))
  
text_area.grid(column = 0, pady = 10, padx = 10)
  
# Placing cursor in the text area
text_area.focus()


d_day=Button(root, text='Consign', bg='red', fg='yellow', font=("Times New Roman", 15), command=open_Toplevel1)
d_day.place(x=180, y=280)
root.mainloop()

