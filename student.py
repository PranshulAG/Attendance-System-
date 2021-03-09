import tkinter
from PIL import ImageTk


class login_system:

    def __init__(self, root):
        self.root = root
        self.root.title("ADMIN LOGIN")
        self.root.geometry("1366x700+0+0")

        self.bg = ImageTk.PhotoImage(file="C:/Users/13054/Downloads/icons/bg.jpg")

        self.user = tkinter.PhotoImage(file="C:/Users/13054/Downloads/icons/user.png")

        self.pass_icon = tkinter.PhotoImage(file="C:/Users/13054/Downloads/icons/pass.png")

        self.logo = tkinter.PhotoImage(file="C:/Users/13054/Downloads/icons/logo.png")

        bglbl = tkinter.Label(self.root, image=self.bg).pack()

        title = tkinter.Label(self.root, text="ADMIN LOGIN", font=("times new roman", 40, "bold"), bg="yellow", fg="red", bd=10,relief=tkinter.GROOVE)
        title.place(x=0, y=0, relwidth=1)
        loginframe = tkinter.Frame(self.root, bg="white")
        loginframe.place(x=400)
        logolbl = tkinter.Label(loginframe, image=self.logo).grid(row=0, column=0, pady=20)


root = tkinter.Tk()
obj = login_system(root)
root.mainloop()
