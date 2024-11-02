from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x890+0+0")
        self.root.title("Face Profiler App")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Background Image
        img = Image.open(r"images\backgroundstu.jpg")
        img = img.resize((1600, 890), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=890)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=150, width=1500, height=600)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Person Details", font=("arial", 16, "bold"), bg="white")
        left_frame.place(x=10, y=10, width=720, height=580)

        # Current course
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Basic Information", font=("arial", 12, "bold"), bg="white")
        current_course_frame.place(x=5, y=20, width=705, height=150)
        
        # Department
        dep_label = Label(current_course_frame, text="Department", font=("arial", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("arial", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "CSE", "EEE", "Civil", "ICE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=20, sticky=W)

        # Current Course Detail
        course_label = Label(current_course_frame, text="Course Details", font=("arial", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("arial", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select", "CSE103", "CSE110", "ENG101", "CSE207", "CSE347")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("arial", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("arial", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2020", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("arial", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("arial", 12, "bold"), state="readonly")
        semester_combo["values"] = ("Select Semester", "Spring", "Summer", "Fall")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Personal Information", font=("arial", 12, "bold"), bg="white")
        class_student_frame.place(x=5, y=185, width=705, height=350)
        
        # Student ID
        studentId_label = Label(class_student_frame, text="ID:", font=("arial", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("arial", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Student name
        studentname_label = Label(class_student_frame, text="Name:", font=("arial", 13, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        studentname_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("arial", 13, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("arial", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("arial", 13, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth
        DOB_label = Label(class_student_frame, text="DOB:", font=("arial", 13, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("arial", 13, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # Email
        Email_label = Label(class_student_frame, text="Email:", font=("arial", 13, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("arial", 13, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Phone
        phone_label = Label(class_student_frame, text="Phone:", font=("arial", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("arial", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
     
        # Address
        address_label = Label(class_student_frame, text="Address:", font=("arial", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("arial", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        
        # Teacher name
        teacher_label = Label(class_student_frame, text="Adviser Name:", font=("arial", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=10, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("arial", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
     
        # Radio Buttons
        self.var_radio = StringVar()  # Single variable to store the value of radio buttons

        radio_btn1 = ttk.Radiobutton(class_student_frame, text="Take Sample", variable=self.var_radio, value="Yes")
        radio_btn1.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        radio_btn2 = ttk.Radiobutton(class_student_frame, text="No Sample", variable=self.var_radio, value="No")
        radio_btn2.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        
        # Buttons frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=430, width=705, height=110)
     
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        save_btn.grid(row=0, column=0, padx=30, pady=12)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        update_btn.grid(row=0, column=1, padx=25, pady=12)
     
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        delete_btn.grid(row=0, column=2, padx=25, pady=12)
     
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        reset_btn.grid(row=1, column=0, padx=10, pady=5)

        take_photo_btn = Button(btn_frame, text="Take Sample", command=self.generate_dataset, width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        take_photo_btn.grid(row=1, column=1, padx=10, pady=5)

        update_photo_btn = Button(btn_frame, text="Update Sample", width=17, font=("arial", 13, "bold"), bg="white", fg="black", borderwidth=2, relief="solid")
        update_photo_btn.grid(row=1, column=2, padx=10, pady=5)
    
        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Person Details", font=("arial", 16, "bold"), bg="white")
        right_frame.place(x=760, y=10, width=720, height=580)

        Search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System", font=("arial", 13, "bold"), bg="white")
        Search_frame.place(x=5, y=15, width=710, height=70)
        
        search_label = Label(Search_frame, text="Search:", font=("arial", 15, "bold"), bg="white", fg="black") 
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        search_combo = ttk.Combobox(Search_frame, font=("arial", 13, "bold"), state="read only", width=15)
        search_combo["values"] = ("Select", "ID", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        
        search_entry = ttk.Entry(Search_frame, width=15, font=("arial", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
     
        search_btn = Button(Search_frame, text="Search", width=12, font=("arial", 12, "bold"), bg="White", fg="black")
        search_btn.grid(row=0, column=3, padx=4)
     
        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("arial", 12, "bold"), bg="white", fg="black")
        showAll_btn.grid(row=0, column=4, padx=4)
        
        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=100, width=710, height=440)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
     
        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Adviser")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    #============== Function Declaration ===============
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
        
    #====================fetch data==============================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()   

    #==============================get cursor======================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_gender.set(data[6])
        self.var_dob.set(data[7])
        self.var_email.set(data[8])
        self.var_phone.set(data[9])
        self.var_address.set(data[10])
        self.var_teacher.set(data[11])
        self.var_radio.set(data[12])

    #========================update function========================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        """UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, 
                        Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s""",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio.get(),
                            self.var_std_id.get()  
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                    self.fetch_data()
                    conn.close()
                else:
                    if not Update:
                        return 
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    #==========================delete function=========================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
                                    
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)       

    #====================reset====================
    def reset_data(self):
        self.var_dep.set("Select Department")                                                                                                                                                                                                                       
        self.var_course.set("Select Course") 
        self.var_year.set("Select Year") 
        self.var_semester.set("Select Semester") 
        self.var_std_id.set("") 
        self.var_std_name.set("") 
        self.var_gender.set("Select Gender") 
        self.var_dob.set("") 
        self.var_email.set("") 
        self.var_phone.set("") 
        self.var_address.set("") 
        self.var_teacher.set("") 
        self.var_radio.set("") 

    #============= Generate data set or Take photo Samples =============
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute(
                    """UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, 
                    Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                    WHERE Student_id=%s""",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio.get(),
                        self.var_std_id.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==================== Load predefined data on face frontals from opencv =======================        

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)  # Corrected here
                    # scaling factor = 1.3
                    # Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                    return None  # Return None if no face is detected

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
