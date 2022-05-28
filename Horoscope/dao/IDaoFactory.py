from abc import ABC, abstractmethod


class IDaoFactory(ABC):
    @abstractmethod
    def get_student_base_repo(self):
        pass
