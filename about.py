import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import studentDetails


class aboutFaceRecognisation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("720x600+0+0")
        self.root.title("Facial Attendance")
        self.root.resizable(False,False)

        aboutProgramLabel = Label(self.root,text="  About Face Recognition Security System",font=("times now roman",27),bg="red",fg="white")
        aboutProgramLabel.place(x=20,y=30)
        aboutFrame = Frame(self.root,bd=2,bg="black")
        aboutFrame.place(x=50,y=150,width=600,height=400)

        aboutDetailsLabelFrame = LabelFrame(aboutFrame,bd=2,width=550,height=350,text="About",bg="white",fg="red")
        aboutDetailsLabelFrame.place(x=25,y=20)

        img = Image.open(r"images/project.png")
        img = img.resize((200,200))
        self.photoImg = ImageTk.PhotoImage(img)
        imgLabel = Label(aboutDetailsLabelFrame,image=self.photoImg,bg="white")
        imgLabel.place(x=170,y=0)

        detailsText = Text(aboutDetailsLabelFrame,height=10,width=60)
        details = "This Project is created By Vishal Chaudhary \n" \
                  "Github Profile - https://github.com/redspider001432 "

        detailsText.place(y=240)
        detailsText.insert(tkinter.END,details)

        helpLabel = Label(detailsText,font=("times now roman",12),bg="blue",fg="white",text="Help and Support:-")
        helpLabel.place(x=0,y=60)

        emailLabel = Label(detailsText,font=("times now roman",10,"bold"),bg="green",fg="white",text="redspider001432@gmail.com")
        emailLabel.place(x=140,y=62)

if __name__ == "__main__":
    root = Tk()
    obj = aboutFaceRecognisation(root)
    root.mainloop()
