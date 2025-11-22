import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import ALL
class button:
    button = tk.Button(text="hi")
    button.pack(pady=20)
class msgbox:
    messagebox.ERROR("Ok", "Ignore")
    messagebox.INFO("Ok", "Cancel")
    messagebox.QUESTION("Yes", "No", "Cancel")
class frame:
    frame = Frame( width=300, height=200, bg='lightblue', relief='raised', bd=5)
    frame.pack(padx=20, pady=20)
class menu:
    def new_file():
        messagebox.showinfo("New File", "Create a new file here.")


    def open_file():
        messagebox.showinfo("Open File", "Open file dialog here.")


    def save_file():
        messagebox.showinfo("Save File", "Save file dialog here.")


    def exit_app():
        quit()


    def cut_text():
        messagebox.showinfo("Cut", "Cut operation performed.")


    def copy_text():
        messagebox.showinfo("Copy", "Copy operation performed.")


    def paste_text():
        messagebox.showinfo("Paste", "Paste operation performed.")


    def about_app():
        messagebox.showinfo("About", "Tkinter Menu Example\nVersion 1.0")


    # Create main window
    root = tk.Tk()
    root.title("Tkinter Menu Example")
    root.geometry("400x300")

    # Create the menu bar
    menubar = tk.Menu(root)

    # ----- File Menu -----
    file_menu = tk.Menu(menubar, tearoff=0)  # tearoff=0 removes dashed line
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)
    menubar.add_cascade(label="File", menu=file_menu)

    # ----- Edit Menu -----
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Cut", command=cut_text)
    edit_menu.add_command(label="Copy", command=copy_text)
    edit_menu.add_command(label="Paste", command=paste_text)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    # ----- Help Menu -----
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about_app)
    menubar.add_cascade(label="Help", menu=help_menu)

    # Attach the menu bar to the root window
    root.config(menu=menubar)

    # Run the application
    root.mainloop()
class loadingbar:
    progress_bar = ttk.Progressbar( orient='horizontal', mode='indeterminate', length=280)
    progress_bar.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
class window:
    root = tk.Tk()

    # Remove the title bar and window frame
    root.overrideredirect(True)

    # Set window size and position (width x height + x_offset + y_offset)
    root.geometry("400x200+100+100")