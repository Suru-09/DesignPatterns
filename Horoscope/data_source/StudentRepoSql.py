from abc import ABC

from data_source.StudentRepoBase import StudentRepoBase
from data_source.SqlLiteHelper import SqlLiteRepo


class StudentRepoSql(StudentRepoBase, ABC):
    def __init__(self, database_path):
        self.__sql_repo = SqlLiteRepo()

    def get_all_students(self):
        return self.__sql_repo.get_students_from_db()
