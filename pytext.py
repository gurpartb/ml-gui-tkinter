# Note: this project was completed by following a tutorial on youtube
# Tutorial Title: How To Build a Text Editor with PYTHON and TKINTER
# Tutorial URL: https://www.youtube.com/watch?v=7PGFin30c4o
# Tutorial Author / Channel: pymike00

import tkinter as tk
from tkinter import filedialog

class Menubar:

    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font = font_specs, tearoff = 0)
        parent.master.config(menu = menubar)

        file_dropdown = tk.Menu(menubar, font = font_specs)
        file_dropdown.add_command(label = "New File", accelerator = "Ctrl+N", command = parent.new_file)
        file_dropdown.add_command(label = "Open File", accelerator = "Ctrl+O", command = parent.open_file)
        file_dropdown.add_command(label = "Save", accelerator = "Ctrl+S", command = parent.save)
        file_dropdown.add_command(label = "Save As", accelerator = "Ctrl+Shift+S", command = parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label = "Exit", command = parent.master.destroy)

        menubar.add_cascade(label = "File", menu = file_dropdown)

class Statusbar:

    def __init__(self, parent):

        font_specs = ("ubuntu", 12)

        self.status = tk.StringVar()
        self.status.set("PyText - 0.1 Gutenberg")

        label = tk.Label(parent.textarea, textvariable = self.status, fg = "black", bg = "lightgrey", anchor = "sw", font = font_specs)
        label.pack(side = tk.BOTTOM, fill = tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0]):
            self.status.set("Your changes have been saved!")
        else:
            self.status.set("PyText - 0.1 Gutenberg")

class PyText:

    def __init__(self, master):
        master.title("Untitled - PyText")
        master.geometry("1200x700")

        font_specs = ("ubuntu", 18)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font = font_specs)
        self.scroll = tk.Scrollbar(master, command = self.textarea.yview)
        self.textarea.configure(yscrollcomman = self.scroll.set)
        self.textarea.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.scroll.pack(side = tk.RIGHT, fill = tk.Y)

        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)

        self.bind_shortcuts()

    def set_window_title(self, name = "Untitled"):
        self.master.title(name + " - PyText")
    
    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension = ".txt",
            filetypes =[("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css"),("CSV Files", "*.csv")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile = "Untitled.txt",
                defaultextension = ".txt")
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)

    def bind_shortcuts(self):
        self.textarea.bind("<Control-n>", self.new_file)
        self.textarea.bind("<Control-o>", self.open_file)
        self.textarea.bind("<Control-s>", self.save)
        self.textarea.bind("<Control-S>", self.save_as)

if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()