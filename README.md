🎓 Student Management System
A comprehensive Student Management System designed to manage student records efficiently. This application allows for the addition of courses, students, results, and viewing reports, utilizing SQLite for database management.

🚀 Features
Course Management: Add and manage courses through a dedicated interface.
Student Management: Enter student details and maintain their records.
Result Management: Input and manage student results easily.
View Reports: Generate and view student reports in a user-friendly format.
Database Management: Utilizes SQLite for efficient data storage and retrieval.
🛠️ Technologies Used
Programming Language: Python
Libraries:
Tkinter: For building the graphical user interface (GUI).
Pillow (PIL): For image handling and manipulation.
SQLite: For database management, enabling persistent storage of data.
📁 Structure
Each button in the application corresponds to a separate module:
Course Management: Managed by course.py, which handles the course addition and modification interface.
Student Management: Handled by student.py, allowing for the entry and management of student data.
Result Management: Implemented in result.py, facilitating the input and management of student results.
Report Viewing: Managed by report.py, which generates and displays reports for students.

Add Course: Click on "COURSE" to open the course management window.
Add Student: Click on "STUDENT" to input student details.
Add Result: Click on "RESULT" to enter student results.
View Student: Click on "VIEW STUDENT" to generate reports.
📅 Database
The application uses SQLite to maintain a database of courses, students, and results, ensuring data persistence across sessions.
