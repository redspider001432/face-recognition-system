from tkinter import *
from time import strftime
from datetime import datetime
import cv2
import mysql.connector
import winsound
from PIL import Image, ImageTk
import winsound


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance")
        self.root.resizable(False,False)

        bg_img = Image.open(r"./images/faceRecognition.jpg")
        resized = bg_img.resize((1520, 800))
        self.detectImage = ImageTk.PhotoImage(resized)

        detectImageLabel = Label(self.root, image=self.detectImage)
        detectImageLabel.place(x=0, y=0)

        img = Image.open(r"./images/gateway.jpg")
        self.photoImg = ImageTk.PhotoImage(img)

        gatewayLogo = Label(self.root, width=350, height=200, bd=2, image=self.photoImg)
        gatewayLogo.place(x=0, y=0)

        btn = Button(self.root, text="Face Recognition", font=("times now roman", 20), bg="darkblue", fg="white",
                     command=self.faceRecog)
        btn.place(x=640, y=700)

    def faceRecog(self):
        def drawBoundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coordinates = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="vishu",
                                               database="face_recognisation", auth_plugin='mysql_native_password')
                myCursor = conn.cursor()

                myCursor.execute("select roll_no from student where stId=" + str(id))
                r = myCursor.fetchone()
                r = "+".join(r)

                myCursor.execute("select name from student where stId=" + str(id))
                n = myCursor.fetchone()
                n = "+".join(n)

                myCursor.execute("select dep from student where stId=" + str(id))
                d = myCursor.fetchone()
                d = "+".join(d)

                myCursor.execute("select Course from student where stId=" + str(id))
                c = myCursor.fetchone()
                c = "+".join(c)

                if confidence > 70:
                    cv2.putText(img, f"RollNo:{r}", (x, y - 65), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(img, f"Name:{n}", (x, y - 45), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    cv2.putText(img, f"Course:{c}", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                    self.attendance(id,r,n,d,c)
                    # self.playSuccessSound()
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # self.playBeepSoud()

                coordinates = [x, y, w, h]
            return coordinates

        def recognition(img, clf, faceCASCADE):
            coordinates = drawBoundary(img, faceCASCADE, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            'C:\\Users\\vishu\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:\\Users\\vishu\\Documents\\faceRecoginition\\classifier.xml")

        videoCapture = cv2.VideoCapture(0)

        while True:
            ret, img = videoCapture.read()
            img = recognition(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1000) == 13:
                cv2.destroyAllWindows()
                videoCapture.release()

    def attendance(self,id,r,n,d,c):
        with open("spider.csv", "r+", newline="\n") as file:
            data = file.readlines()
            nameList = []
            for line in data:
                entry = line.split((","))
                nameList.append(entry[0])
            if((r not in nameList)) and ((n not in nameList)) and ((d not in nameList)) and ((c not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dT = now.strftime("%H:%M:%S")
                file.writelines(f"\n{id},{r},{n},{d},{c},{dT},{d1},Present")

    def playBeepSoud(self):
        frequency = 2000
        duration = 2000

        winsound.Beep(frequency,duration)

    def playSuccessSound(self):
        winsound.PlaySound("success.wav",winsound.SND_FILENAME)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
