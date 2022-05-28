from abc import ABC
import xml.etree.ElementTree as ET


from data_source.StudentRepoBase import StudentRepoBase
from student.Student import Student


class StudentRepoXML(StudentRepoBase, ABC):
    def __init__(self, file_path):
        self.__tree = ET.parse(file_path)
        self.__root = self.__tree.getroot()
        self.__student_list = []

    def get_all_students(self):
        for student in self.__root:
            for sub_tags in student:
                if sub_tags.tag == "name":
                    self.__student_list.append(Student(str(sub_tags.text)))

        # for x in self.__student_list:
        #     print(x.name)
        return self.__student_list
