from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x890+0+0")
        self.root.title("Face Profiler App")

        # Background Image
        img = Image.open(r"images\backgroundtrain1.jpg")
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

        # Train Button
        img2 = Image.open(r"images\train2.jpg")
        img2 = img2.resize((200, 200), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        border_frame1 = Frame(bg_img, bg="#1e1e1e", width=frame_width, height=frame_width)
        border_frame1.place(x=start_x, y=y_position)

        b1 = Button(border_frame1, image=self.photoimg2, cursor="hand2", command=self.train_classifier)
        b1.place(x=2, y=2, width=button_width, height=button_width)

        b1_1 = Label(bg_img, text="Train Data", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b1_1.place(x=start_x + 2, y=y_position + frame_width + 10, width=button_width, height=40)

        # Collect Data Button
        img6 = Image.open(r"images\camera.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        border_frame5 = Frame(bg_img, bg="#1e1e1e", width=frame_width, height=frame_width)
        border_frame5.place(x=start_x + frame_width + gap, y=y_position)

        b5 = Button(border_frame5, image=self.photoimg6, cursor="hand2", command=self.open_img)
        b5.place(x=2, y=2, width=button_width, height=button_width)

        b5_1 = Label(bg_img, text="Dataset", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b5_1.place(x=start_x + frame_width + gap + 2, y=y_position + frame_width + 10, width=button_width, height=40)

        # Logout Button
        img7 = Image.open(r"images\exit.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        border_frame6 = Frame(bg_img, bg="#1e1e1e", width=frame_width, height=frame_width)
        border_frame6.place(x=start_x + 2 * (frame_width + gap), y=y_position)

        b6 = Button(border_frame6, image=self.photoimg7, cursor="hand2", command=root.quit)
        b6.place(x=2, y=2, width=button_width, height=button_width)

        b6_1 = Label(bg_img, text="Exit", font=("arial", 15, "bold"), fg="white", bg="#1e1e1e")
        b6_1.place(x=start_x + 2 * (frame_width + gap) + 2, y=y_position + frame_width + 10, width=button_width, height=40)
    
    def train_classifier(self):
    # Directory containing the training images
        path = "data"

        def getImageID(path):
        # Get the list of image paths
            imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
            faces = []
            ids = []

        # Loop through all the image paths
            for imagePath in imagePaths:
            # Convert the image to grayscale
                faceImage = Image.open(imagePath).convert('L')
                faceNP = np.array(faceImage, 'uint8')  # Convert the PIL image to a numpy array

            # Extract the ID from the image filename
                Id = int(os.path.split(imagePath)[-1].split(".")[1])

                faces.append(faceNP)
                ids.append(Id)

            # Display the training image
                cv2.imshow("Training", faceNP)
                cv2.waitKey(1)

            return ids, faces

    # Fetch the face data and corresponding IDs
        ids, facedata = getImageID(path)

    # Create an LBPH face recognizer and train it with the face data
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(facedata, np.array(ids))
        recognizer.write("classifier.xml")  

        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Training Completed!")

 

    def open_img(self):
        os.startfile("data")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
