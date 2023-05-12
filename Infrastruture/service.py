
from abc import ABC, abstractmethod
from CRUD.Model.entity import Category
from CRUD.Infrastruture.repository import CategoryRepository
from pymongo import errors
from pprint import pprint
from bson.objectid import ObjectId


class BaseCategoryService(ABC):

    @abstractmethod
    def CreateCategory(self, name, description) -> str: pass

    @abstractmethod
    def ListCategory(self): pass

    @abstractmethod
    def GetById(self, categoryId): pass

    @abstractmethod
    def UpdateCategory(self, categoryId, name, description): pass

    @abstractmethod
    def DeleteCategory(self, categoryId): pass


class CategoryService(BaseCategoryService):

    def CreateCategory(self, name, description) -> str:
        try:
            categoryRepository = CategoryRepository()

            categoryItem = Category(name, description)

            categoryRepository.create(categoryItem.__dict__)

            return f'{categoryItem.name} has been added..!'

        except errors as err:
            return f'Caught a error..!\n{err.__doc__}'

    def ListCategory(self):
        categoryRepository = CategoryRepository()

        result = categoryRepository.list()

        if result.collection.__sizeof__() > 0:
            print(f'{result.collection.__sizeof__()} item was found.\n')
            for item in result:
                pprint(item)
        else:
            print('There is no item.')

    def GetById(self, categoryId):
        categoryRepository = CategoryRepository()

        result = categoryRepository.getDefault(categoryId)

        return result

    def UpdateCategory(self, categoryId, name, description):
        try:
            categoryRepository = CategoryRepository()

            filterValue = {"_id": ObjectId(categoryId)}
            newValues = {'$set': {
                'name': name,
                'description': description
            }}

            result = categoryRepository.update(filterValue, newValues)

            return f'{name} has been edited.\n{result.modified_count} row was effected..!'

        except errors as err:
            return f'Caught a error..!\n{err.__doc__}'

    def DeleteCategory(self, categoryId):
        try:
            categoryRepository = CategoryRepository()

            filterValue = {"_id": ObjectId(categoryId)}

            result = categoryRepository.delete(filterValue)

            return f'Delete process was successfull..!\n{result.deleted_count} row was affected'

        except errors as err:
            return f'Caught a error..!\n{err.__doc__}'
