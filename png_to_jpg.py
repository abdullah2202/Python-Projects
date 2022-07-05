from importlib.machinery import SourceFileLoader
import tkinter as tk
from tkinter import filedialog
from creds import tinfiy_api
import tinify

tinify.key = tinfiy_api.tf_api
filetypes = [('PNG','*.png'),('JPG','*.jpg'),('WEBP','*.webp')]

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="Image Converter with Tinify", bg='azure3', wraplength=250)
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def convert():
    global source
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=filetypes)
    source.to_file(export_file_path)

def getPNG():
    global source
    import_file_path = filedialog.askopenfilename()
    source = tinify.from_file(import_file_path)

browse_png = tk.Button(text="Select Image file", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)

saveasbutton = tk.Button(text="Tinify to PNG/JPG/WebP", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()
