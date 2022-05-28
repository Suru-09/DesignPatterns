from abc import ABC, abstractmethod


class IBusinessLogic(ABC):

    @abstractmethod
    def execute(self, factory_type):
        pass
