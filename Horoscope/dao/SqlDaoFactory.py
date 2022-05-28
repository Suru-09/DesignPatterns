from abc import ABC

from dao.IDaoFactory import IDaoFactory
from data_source.StudentRepoSql import StudentRepoSql


class SqlDaoFactory(IDaoFactory, ABC):

    def __init__(self, database_path='sql_lite_database/sql.db'):
        self.__database_path = database_path

    def get_student_base_repo(self):
        return StudentRepoSql(self.__database_path)
