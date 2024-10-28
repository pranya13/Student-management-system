import sqlite3
def create_db():
    con = sqlite3.connect(database="lms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS  course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, Charges text, Description text) ")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS  student(roll INTEGER PRIMARY KEY AUTOINCREMENT, Name text, Email text, Gender text, DOB text, Contact text, Admission text,Course text, State text, City text, Pin text, Address text) ")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS  result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, marks_ob text, full_marks text, per text) ")
    con.commit()

    con.close()
create_db()    