from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x890+0+0")
        self.root.title("Face Profiler App")

        # Background Image
        img = Image.open(r"images\background3.jpg")
        img = img.resize((1600, 890), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=890)

        # Person Button
        img2 = Image.open(r"images\person.jpg")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Centering the frames horizontally with a minimum gap of 200 pixels between each
        total_width = 3 * 205 + 2 * 200
        start_x = (1600 - total_width) // 2
        y_position = 170  # y position for frames

        border_frame1 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame1.place(x=start_x, y=y_position)

        b1 = Button(border_frame1, image=self.photoimg2, command=self.student_details, cursor="hand2")
        b1.place(x=2, y=2, width=200, height=200)

        b1_1 = Label(bg_img, text="Person Details", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b1_1.place(x=start_x + 2, y=y_position + 205 + 10, width=200, height=40)

        # Detect Face Button
        img3 = Image.open(r"images\facedetector.jpg")
        img3 = img3.resize((250, 200), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        border_frame2 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame2.place(x=start_x + 205 + 200, y=y_position)  # 200 pixels between frames

        b2 = Button(border_frame2, image=self.photoimg3, cursor="hand2", command=self.face_data)
        b2.place(x=2, y=2, width=200, height=200)

        b2_1 = Label(bg_img, text="Face Detector", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b2_1.place(x=start_x + 205 + 202, y=y_position + 205 + 10, width=200, height=40)

        # Attend Time Button
        img4 = Image.open(r"images\attend.jpg")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        border_frame3 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame3.place(x=start_x + 2 * (205 + 200), y=y_position)  # 200 pixels between frames

        b3 = Button(border_frame3, image=self.photoimg4, cursor="hand2", command=self.atted_time)
        b3.place(x=2, y=2, width=200, height=200)

        b3_1 = Label(bg_img, text="Attend Time", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b3_1.place(x=start_x + 2 * (205 + 200) + 2, y=y_position + 205 + 10, width=200, height=40)

        # Train Data Button
        img5 = Image.open(r"images\traindata.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        border_frame4 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame4.place(x=start_x, y=y_position + 300)  # 300 pixels below the first row

        b4 = Button(border_frame4, image=self.photoimg5, cursor="hand2", command=self.train_data)
        b4.place(x=2, y=2, width=200, height=200)

        b4_1 = Label(bg_img, text="Train Data", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b4_1.place(x=start_x + 2, y=y_position + 300 + 205 + 10, width=200, height=40)

        # DataSet Button
        img6 = Image.open(r"images\collectdata.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        border_frame5 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame5.place(x=start_x + 205 + 200, y=y_position + 300)  # 300 pixels below the first row

        b5 = Button(border_frame5, image=self.photoimg6, cursor="hand2", command=self.open_img)
        b5.place(x=2, y=2, width=200, height=200)

        b5_1 = Button(bg_img, text="Dataset", command=self.open_img, font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b5_1.place(x=start_x + 205 + 202, y=y_position + 300 + 205 + 10, width=200, height=40)

        # Logout Button
        img7 = Image.open(r"images\logout2.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        border_frame6 = Frame(bg_img, bg="white", width=205, height=205)
        border_frame6.place(x=start_x + 2 * (205 + 200), y=y_position + 300)  # 300 pixels below the first row

        b6 = Button(border_frame6, image=self.photoimg7, cursor="hand2", command=self.isExit)
        b6.place(x=2, y=2, width=200, height=200)

        b6_1 = Label(bg_img, text="Log Out", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b6_1.place(x=start_x + 2 * (205 + 200) + 2, y=y_position + 300 + 205 + 10, width=200, height=40)

    #====== Function =======
    def open_img(self):
        os.startfile("data")

    def isExit(self):
        self.isExit=tkinter.messagebox.askyesno("Facial Profiler", "Are you sure exit?",parent=self.root)
        if self.isExit > 0:
            self.root.destroy()
        else:
            return

    #================= Function Button ===================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def atted_time(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
