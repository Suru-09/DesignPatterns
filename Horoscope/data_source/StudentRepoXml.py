from abc import ABC
import xml.etree.ElementTree as ET


from data_source.StudentRepoBase import StudentRepoBase
from student.Student import Student


class StudentRepoXML(StudentRepoBase, ABC):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__tree = ET.parse(file_path)
        self.__root = self.__tree.getroot()
        self.__student_list = []

    def get_all_students(self):
        for student in self.__root:
            for sub_tags in student:
                if sub_tags.tag == "name":
                    self.__student_list.append(Student(str(sub_tags.text)))
        return self.__student_list

    def get_student_after_name(self, name):
        for student in self.__root:
            for sub_tags in student:
                if sub_tags.tag == "name":
                    if (str(sub_tags.text)) == name:
                        return Student(name)
        return None

    def add_student(self, student):
        if self.get_student_after_name(student.name) is None:
            element = ET.Element("student")
            sub_el = ET.SubElement(element, "name")
            sub_el.text = student.name
            self.__root.insert(0, element)
            ET.indent(self.__tree, '    ')
            self.__tree.write(self.__file_path, encoding="utf-8", xml_declaration=True)
        else:
            print("The student that you are trying to add already exists!\n")


