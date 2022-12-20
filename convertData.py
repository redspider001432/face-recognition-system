import os
from tkinter import *
from tkinter import ttk, messagebox
from train import *

import cv2
from PIL import Image, ImageTk
import numpy as np

class convertData:
    def __init__(self, root):
        self.root = root
        self.root.geometry("730x400+0+0")
        self.root.title("Facial Attendance")
        self.root.resizable(False,False)

        convertLabel = Label(self.root,text="Convert Images into Binary Code",font=("times now roman",35),bg="black",fg="green")
        convertLabel.place(x=20,y=70)

        btn = Button(self.root,text="Start",bg="red",fg="white",font=("times now roman",20),cursor="hand2",command=self.convertClassifier)
        btn.place(x=320,y=190)







    def convertClassifier(self):
        dataDir = ("data")
        path = [os.path.join(dataDir,file) for file in os.listdir(dataDir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imgNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Converting",imgNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Results","Converting completed!!!!")





if __name__ == "__main__":
    root = Tk()
    obj = convertData(root)
    root.mainloop()