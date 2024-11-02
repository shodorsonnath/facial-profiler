from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import winsound

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x890+0+0")
        self.root.title("Face Profiler App")

        # Background Image
        img = Image.open(r"images\backgroundface.jpg")
        img = img.resize((1600, 890), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=890)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=150, width=1500, height=600)

        # Center calculation
        frame_width = 205
        button_width = 200
        gap = 200
        total_width = 3 * frame_width + 2 * gap
        start_x = (1600 - total_width) // 2
        y_position = 250

        # Detect Button
        img2 = Image.open(r"images\detectp.jpg")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        border_frame1 = Frame(bg_img, bg="#1e1e1e", width=frame_width, height=frame_width)
        border_frame1.place(x=start_x, y=y_position)

        b1 = Button(border_frame1, image=self.photoimg2, cursor="hand2", command=self.face_recognition)
        b1.place(x=2, y=2, width=button_width, height=button_width)

        b1_1 = Label(bg_img, text="Detect Person", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b1_1.place(x=start_x + 2, y=y_position + frame_width + 10, width=button_width, height=40)

        # Train Data Button
        img6 = Image.open(r"images\train2.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        border_frame5 = Frame(bg_img, bg="white", width=frame_width, height=frame_width)
        border_frame5.place(x=start_x + frame_width + gap, y=y_position)

        b5 = Button(border_frame5, image=self.photoimg6, cursor="hand2", command=self.train_classifier)
        b5.place(x=2, y=2, width=button_width, height=button_width)

        b5_1 = Label(bg_img, text="Train Data", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b5_1.place(x=start_x + frame_width + gap + 2, y=y_position + frame_width + 10, width=button_width, height=40)

        # Logout Button
        img7 = Image.open(r"images\exit.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        border_frame6 = Frame(bg_img, bg="white", width=frame_width, height=frame_width)
        border_frame6.place(x=start_x + 2 * (frame_width + gap), y=y_position)

        b6 = Button(border_frame6, image=self.photoimg7, cursor="hand2", command=root.quit)
        b6.place(x=2, y=2, width=button_width, height=button_width)

        b6_1 = Label(bg_img, text="Exit", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b6_1.place(x=start_x + 2 * (frame_width + gap) + 2, y=y_position + frame_width + 10, width=button_width, height=40)

    #================== Train Function ==================
    def train_classifier(self):
        data_dir = "data" 
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') 
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)

        # Convert ids to a numpy array
        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows() 
        messagebox.showinfo("Result", "Dataset Training Completed!")

    # ============================== ATTENDANCE ==================================

    def mark_attendance(self, id, name):
        with open("attend.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if id not in name_list:
                now = datetime.now()  
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{name},{dtString},{d1},Present")

    # ====================== Face Recognition =======================
    def face_recognition(self):

        def detect_and_display(frame, face_classifier, recognizer, name_list):
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
            faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)  # Detect faces

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around the face

            # Predict the ID of the detected face
                id, confidence = recognizer.predict(gray_image[y:y + h, x:x + w])

            # Adjust the condition to handle recognized and unrecognized faces
                if confidence < 50:  # Recognized face (lower confidence is better)
                    if 0 <= id < len(name_list):  # Check if id is a valid index
                        name = name_list[id]
                    # Mark attendance
                        self.mark_attendance(id, name)
                    else:
                        name = "Unknown"
                        winsound.Beep(1000, 500)
                else:  # Unrecognized face
                    name = "Unknown"
                    winsound.Beep(1000, 500)
            
            # Display the ID and Name on the frame
                cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

            return frame

    # Load the pre-trained face detection model
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Load the trained face recognizer model
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")  # Updated to use "Trainer.yml"

    # Define a list of names manually
        name_list = ["Unknown", "Shodorson"]  # Ensure the list length matches the IDs

    # Initialize webcam
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

        # Detect and display the faces and recognized names
            frame = detect_and_display(frame, face_classifier, recognizer, name_list)

        # Display the resulting frame
            cv2.imshow("Face Recognition", frame)

        # Check for 'q' key to quit
            k = cv2.waitKey(1)
            if k == ord("q"):
                break

    # Release the video capture object and close all windows
        video_capture.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
