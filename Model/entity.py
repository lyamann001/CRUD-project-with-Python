
from enum import Enum
from datetime import datetime


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__createDate = ''
        self.__status = ''

    def setValue(self):
        self.__createDate = datetime.now()
        self.__status = Status.Active.value


class Category(BaseEntity):
    def __init__(self, name, description):
        super(Category, self).__init__()
        self.setValue()
        self.name = name
        self.desciption = description


class Product(BaseEntity):
    pass
