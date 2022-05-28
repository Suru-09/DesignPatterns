from abc import ABC
import sys

from utils.FactoryType import FactoryType
from dao.XmlDaoFactory import XmlDaoFactory
from dao.SqlDaoFactory import SqlDaoFactory
from dao.IDaoFactory import IDaoFactory


class DaoFactory(IDaoFactory, ABC):

    @staticmethod
    def get_dao_factory(which_factory):
        if which_factory == FactoryType.XML:
            return XmlDaoFactory()
        elif which_factory == FactoryType.SQL:
            return SqlDaoFactory()
        else:
            print("Given factory type is INVALID!\n")
            sys.exit()
