from abc import ABC, abstractmethod


class StudentRepoBase(ABC):
    @abstractmethod
    def get_all_students(self):
        pass
