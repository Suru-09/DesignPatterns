from abc import ABC

from dao.IDaoFactory import IDaoFactory
from data_source.StudentRepoXml import StudentRepoXML


class XmlDaoFactory(IDaoFactory, ABC):

    def __init__(self, file_path="xml_testing_files/students_1.xml"):
        self.__file_path = file_path

    def get_student_base_repo(self):
        return StudentRepoXML(self.__file_path)
