from abc import ABC, abstractmethod


class StudentRepoBase(ABC):
    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def get_student_after_name(self, name):
        pass

    @abstractmethod
    def add_student(self, student):
        pass
