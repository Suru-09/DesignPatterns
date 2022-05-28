from abc import ABC

from data_source.IStudentRepoBase import IStudentRepoBase
from data_source.SqlLiteHelper import SqlLiteRepo


class StudentRepoSql(IStudentRepoBase, ABC):
    def __init__(self, database_path):
        self.__sql_repo = SqlLiteRepo()

    def get_all_students(self):
        return self.__sql_repo.get_students_from_db()

    def get_student_after_name(self, name):
        return self.__sql_repo.get_student_after_name(name)

    def add_student(self, student):
        self.__sql_repo.add_student_in_database(student)


