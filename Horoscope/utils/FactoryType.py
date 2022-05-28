from enum import Enum


class FactoryType(Enum):
    XML = 1
    SQL = 2
    NOT_DEFINED = -1

    @classmethod
    def _missing_(cls, value):
        return FactoryType.NOT_DEFINED
