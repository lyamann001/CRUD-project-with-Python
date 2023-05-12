
from abc import ABC, abstractmethod
from CRUD.Infrastruture.context import categoryCollection
from bson.objectid import ObjectId


class AbstractBaseRepository(ABC):

    @abstractmethod
    def create(self, item: dict): pass

    @abstractmethod
    def update(self, filterValue: dict, newValues: dict): pass

    @abstractmethod
    def list(self): pass

    @abstractmethod
    def delete(self, item: dict): pass

    @abstractmethod
    def getDefault(self, param): pass


class CategoryRepository(AbstractBaseRepository):

    def create(self, item: dict):
        categoryCollection.insert_one(item)

    def update(self, filterValue: dict, newValues: dict):
        result = categoryCollection.update_one(filterValue, newValues)
        return result

    def list(self):
        return categoryCollection.find()

    def delete(self, item: dict):
        result = categoryCollection.delete_one(item)
        return result

    def getDefault(self, param):
        return categoryCollection.find_one({"_id": ObjectId(param)})


class ProductRepository(AbstractBaseRepository):

    def create(self, item: dict):
        productCollection.Insert_One(item)

    def update(self, filterValue: dict, newValues: dict):
        pass

    def list(self):
        pass

    def delete(self, item: dict):
        pass

    def getDefault(self, param):
        pass