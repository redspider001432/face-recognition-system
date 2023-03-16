from tkinter import *
from tkinter import ttk, messagebox
from main import *
import mysql.connector
from PIL import Image, ImageTk


class loginSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Security")
        self.username = StringVar()
        self.password = StringVar()
        # self.root.resizable(False, False)

        bg_img = Image.open(r"images/background.jpg")
        bg_img = bg_img.resize((1530, 790))
        self.bg = ImageTk.PhotoImage(bg_img, Image.ANTIALIAS)
        imageLabel = Label(self.root, image=self.bg)
        imageLabel.pack()

        mainFrame = Frame(imageLabel, bd=2, width=300, height=500, bg="black")
        mainFrame.place(x=620, y=150)

        label1Img = Image.open(r"images/background1.jpg")
        label1Img = label1Img.resize((600, 600))
        self.labelImg = ImageTk.PhotoImage(label1Img, Image.ANTIALIAS)
        label1 = Label(mainFrame, width=300, height=500, image=self.labelImg)
        label1.pack()

        headingLabel = Label(label1, text="------Face Recognition------", fg="green", font=("times new roman", 20),
                             bg="black")
        headingLabel.place(x=0)

        loginLabel = Label(label1, text="Username: ", bg="black", fg="white", font=("times new roman", 14))
        loginLabel.place(x=0, y=100)
        self.loginEntry = ttk.Entry(label1, width=30,textvariable=self.username)
        self.loginEntry.place(x=100, y=104)

        passwordLabel = Label(label1, text="Password: ", bg="black", fg="white", font=("times new roman", 14))
        passwordLabel.place(x=0, y=150)
        self.passwordEntry = ttk.Entry(label1, width=30,textvariable=self.password)
        self.passwordEntry.place(x=100, y=154)

        btn = Button(label1, text="Login", bg="black", fg="white", font=("times new roman", 12,"bold"), width=32,
                     cursor="hand2", activebackground="green", command=self.login)
        btn.place(x=0, y=220)

    def login(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                           auth_plugin='mysql_native_password',database="face_recognisation")

            myCursor = conn.cursor()
            myCursor.execute("select * from gateway_portal where id = 1")
            data = myCursor.fetchone()
            username = data[1]
            password = data[2]
            if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror("Error","All fields are required!!")
            elif self.password.get() == password and self.username.get() == username:
                messagebox.showinfo("success",f"Welcome {username}")
                self.loginSuccess()
                self.root.state("withdraw")
            else:
                messagebox.showerror("Error","Wrong Username or Password")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def loginSuccess(self):
        self.new_window = Toplevel(root)
        self.windows = FaceRecognitionSystem(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = loginSystem(root)
    root.mainloop()
