from abc import ABC
from datetime import datetime
from businness.IBusinessLogic import IBusinessLogic
from dao.DaoFactory import DaoFactory


class Horoscope(IBusinessLogic, ABC):

    def __init__(self, student_list=None):
        self.__student_list = student_list
        self.__vowels = ('a', 'e', 'i', 'o', 'u')

    def __is_good_day(self, student_name) -> bool:
        current_day_of_month = int(datetime.now().strftime("%d"))
        no_of_vowels = 0

        for letter in student_name.lower():
            if letter in self.__vowels:
                no_of_vowels += 1

        if current_day_of_month % no_of_vowels == 0:
            return True
        return False

    def predict_all_students(self):
        for student in self.__student_list:
            if self.__is_good_day(student.name):
                day_type_string = "GOOD"
            else:
                day_type_string = "BAD"
            print(student.name + " will have a " + day_type_string + " day")

    def execute(self, factory_type):
        student_repo = DaoFactory.get_dao_factory(factory_type).get_student_base_repo()
        self.__student_list = student_repo.get_all_students()
        self.predict_all_students()
