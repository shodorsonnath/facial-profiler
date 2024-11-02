from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =============variables===============
        self.var_atten_id = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Background Image
        img = Image.open(r"images\backgroundstu.jpg")
        img = img.resize((1600, 890), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1600, height=890)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=12, y=150, width=1500, height=600)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Person Details", font=("arial", 18, "bold"), bg="white")
        left_frame.place(x=10, y=20, width=720, height=520)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=15, y=20, width=690, height=370)

        # Label and Entry
        # id
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentname_label = Label(left_inside_frame, text="Name:", font=("arial", 13, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)

        studentname_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20, font=("arial", 13, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("arial", 13, "bold"), bg="white")
        time_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=20, font=("arial", 13, "bold"))
        time_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("arial", 13, "bold"), bg="white")
        date_label.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=20, font=("arial", 13, "bold"))
        date_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status:", font=("comicsansns", 11, "bold"), bg="white")
        attendanceLabel.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, width=20, font=("comicsansns", 11, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=4, column=1, padx=10, pady=8, sticky=W)
        self.atten_status.current(0)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=300, width=680, height=35)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 12, "bold"), bg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 12, "bold"), bg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", command=self.update, width=17, font=("times new roman", 12, "bold"), bg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset, width=17, font=("times new roman", 12, "bold"), bg="white")
        reset_btn.grid(row=0, column=3)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("arial", 18, "bold"), bg="white")
        Right_frame.place(x=750, y=20, width=720, height=520)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=8, y=20, width=700, height=455)

        # Scrollbar Table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "name", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="ID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Status")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # =================fetch Data==================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()  # Clear existing data
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        if row:
            self.var_atten_id.set(row[0])
            self.var_atten_name.set(row[1])
            self.var_atten_time.set(row[2])
            self.var_atten_date.set(row[3])
            self.var_atten_attendance.set(row[4])

    def reset(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

    def update(self):
        selected = self.AttendanceReportTable.focus()  # Get the selected item
        if not selected:
            messagebox.showerror("Error", "No record selected", parent=self.root)
            return

        # Update the selected item with new values from entry fields
        self.AttendanceReportTable.item(selected, values=(self.var_atten_id.get(),
                                                          self.var_atten_name.get(),
                                                          self.var_atten_time.get(),
                                                          self.var_atten_date.get(),
                                                          self.var_atten_attendance.get()))

        # Optional: Update the CSV data in memory if you want to keep it in sync
        for i in range(len(mydata)):
            if mydata[i][0] == self.var_atten_id.get():
                mydata[i] = [self.var_atten_id.get(), self.var_atten_name.get(), self.var_atten_time.get(), self.var_atten_date.get(), self.var_atten_attendance.get()]
                break

        messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
