import sqlite3

from student.Student import Student


class SqlLiteRepo:
    student_list = [
        ('Georgel',),
        ('Alina',),
        ('Popa',),
        ('Dorian',),
        ('Geoergica',),
        ('Catalin',),
        ('Catalina',),
        ('Lina',),
    ]

    def __init__(self, database_path='sql_lite_database/sql.db', student_list=None):
        if student_list is None:
            self.__student_list = self.student_list
        self.__connection = sqlite3.connect(database_path)
        self.__current = self.__connection.cursor()
        self.__initialize_student_table()

    def __initialize_student_table(self):
        # self.__current.execute("drop table IF EXISTS student")

        self.__current.execute("create table IF NOT EXISTS student (name)")

        # Populate table with default student_list if they are not present there
        for student in self.__student_list[0]:
            if self.get_student_after_name(student) is None:
                self.__current = self.__connection.cursor()
                self.__current.executemany("INSERT INTO student values (?)", student)
        # self.__current.executemany("INSERT INTO student values (?)", self.__student_list)

        self.__connection.commit()
        self.__current.close()

    def get_students_from_db(self):
        tmp_student_list = []
        # opening the cursor again (it has been closed after table initialization)
        self.__current = self.__connection.cursor()
        for row in self.__current.execute('SELECT * FROM student'):
            tmp_student_list.append(Student(row[0]))
        self.__current.close()
        return tmp_student_list

    def get_student_after_name(self, name):
        self.__current = self.__connection.cursor()
        for row in self.__current.execute('SELECT * FROM student WHERE name = ?', (name,)):
            self.__current.close()
            if row is not None:
                return Student(row[0])
            else:
                return None

    def add_student_in_database(self, student):
        if self.get_student_after_name(student.name) is None:
            self.__current = self.__connection.cursor()
            self.__current.execute("INSERT INTO student values (?)", (student.name,))
            self.__connection.commit()
            self.__current.close()
        else:
            print("The student that you're trying to add already exists!\n")
