from tkinter import *
from PIL import Image, ImageTk  # type: ignore
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Logo and Title Bar with updated color and uppercase styling
        logo_image = Image.open("logo.jpg.png")
        resized_logo = logo_image.resize((50, 50))
        self.logo_dash = ImageTk.PhotoImage(resized_logo)
        title = Label(self.root, text="  STUDENT MANAGEMENT SYSTEM", image=self.logo_dash, compound=LEFT,
                      font=("Tahoma", 26, "bold"), bg="#004d80", fg="white", padx=10)
        title.place(x=0, y=0, relwidth=1, height=60)

        # Menu Frame with single-line buttons
        M_Frame = Frame(self.root, bg="white")
        M_Frame.place(x=10, y=70, width=1330, height=80)

        # Adjusted button style to uppercase, in a single row
        btn_course = Button(M_Frame, text="COURSE", font=("goudy old style", 18, "bold"), bg="#006699", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=10, y=10, width=310, height=60)

        btn_student = Button(M_Frame, text="STUDENT", font=("goudy old style", 18, "bold"), bg="#006699", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=330, y=10, width=310, height=60)

        btn_result = Button(M_Frame, text="RESULT", font=("goudy old style", 18, "bold"), bg="#006699", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=650, y=10, width=310, height=60)

        btn_view = Button(M_Frame, text="VIEW STUDENT", font=("goudy old style", 18, "bold"), bg="#006699", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=970, y=10, width=310, height=60)

        # Background image resized to cover more space
        self.bg_img = Image.open("bg.png")
        self.bg_img = self.bg_img.resize((920, 400))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=220, y=180, width=920, height=400)

        # Footer with adjusted font size for a more cohesive look
        footer = Label(self.root, text="STUDENT MANAGEMENT SYSTEM\nContact us for any technical issue: 987xx", 
                       font=("Tahoma", 14), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
