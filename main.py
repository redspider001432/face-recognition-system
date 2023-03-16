from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from attendance import AttendanceSystem
from faceRecognition import FaceRecognition
from student import studentDetails
from about import aboutFaceRecognisation
from convertData import convertData


class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Security")

        # background
        img1 = Image.open(r"./images/gateway.jpg")
        img1 = img1.resize((1530, 710), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(img1)

        bg_image = Label(self.root, image=self.photoImg1)
        bg_image.place(x=0, y=70, width=1530, height=700)

        labelledTitle = Label(self.root, text="Facial Security System", font=("times new roman", 35, "bold"),
                              bg="white", fg="red")
        labelledTitle.place(x=0, y=0, width=1530, height=45)

        # Button1 student details
        img2 = Image.open(r"./images/student.png")
        img2 = img2.resize((96, 96), Image.ANTIALIAS)
        self.photoImg2 = ImageTk.PhotoImage(img2)

        button1 = Button(bg_image, image=self.photoImg2,command=self.student_details,cursor="hand2")
        button1.place(x=200, y=50, width=220, height=220)

        button1_1 = Button(bg_image, text="Student Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white")
        button1_1.place(x=200, y=250, width=220, height=20)



        # Button2 Face Detector
        img3 = Image.open(r"./images/facedetect.png")
        img3 = img3.resize((96, 96), Image.ANTIALIAS)
        self.photoImg3 = ImageTk.PhotoImage(img3)

        button1 = Button(bg_image, image=self.photoImg3, cursor="hand2",command=self.faceRecognition)
        button1.place(x=700, y=50, width=220, height=220)

        button1_1 = Button(bg_image, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white",command=self.faceRecognition)
        button1_1.place(x=700, y=250, width=220, height=20)

        # Button3 Attendance
        img4 = Image.open(r"./images/attendance.png")
        img4 = img4.resize((96, 96), Image.ANTIALIAS)
        self.photoImg4 = ImageTk.PhotoImage(img4)

        button1 = Button(bg_image, image=self.photoImg4, cursor="hand2",command=self.markAttendance)
        button1.place(x=1200, y=50, width=220, height=220)

        button1_1 = Button(bg_image, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white",command=self.markAttendance)
        button1_1.place(x=1200, y=250, width=220, height=20)

        # Button4 About
        img5 = Image.open(r"./images/about.png")
        img5 = img5.resize((96, 96), Image.ANTIALIAS)
        self.photoImg5 = ImageTk.PhotoImage(img5)

        button1 = Button(bg_image, image=self.photoImg5, cursor="hand2",command=self.about)
        button1.place(x=280, y=450, width=220, height=220)

        button1_1 = Button(bg_image, text="About", cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white",command=self.about)
        button1_1.place(x=280, y=650, width=220, height=20)

        # Button5 About

        img6 = Image.open(r"./images/convert.png")
        img6 = img6.resize((96, 96), Image.ANTIALIAS)
        self.photoImg6 = ImageTk.PhotoImage(img6)

        button1 = Button(bg_image, image=self.photoImg6, cursor="hand2",command=self.convert_data)
        button1.place(x=650, y=450, width=220, height=220)

        button1_1 = Button(bg_image, text="Convert Data", cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white",command=self.convert_data)
        button1_1.place(x=650, y=650, width=220, height=20)

        img7 = Image.open(r"./images/exit.png")
        img7 = img7.resize((96, 96), Image.ANTIALIAS)
        self.photoImg7 = ImageTk.PhotoImage(img7)

        button1 = Button(bg_image, image=self.photoImg7, cursor="hand2",command=self.exit)
        button1.place(x=1050, y=450, width=220, height=220)

        button1_1 = Button(bg_image, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
                           bg="blue", fg="white",command=self.exit)
        button1_1.place(x=1050, y=650, width=220, height=20)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.window = studentDetails(self.new_window)

    def convert_data(self):
        self.new_window = Toplevel(self.root)
        self.window = convertData(self.new_window)

    def about(self):
        self.new_window = Toplevel(self.root)
        self.window = aboutFaceRecognisation(self.new_window)

    def faceRecognition(self):
        self.new_window = Toplevel(self.root)
        self.window = FaceRecognition(self.new_window)

    def markAttendance(self):
        self.new_window = Toplevel(self.root)
        self.window = AttendanceSystem(self.new_window)

    def exit(self):
        exit = messagebox.askyesno("Exit","Are you sure You want to exit",parent=self.root)
        if exit:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
