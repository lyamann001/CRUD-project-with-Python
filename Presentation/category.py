
from CRUD.Infrastruture.service import CategoryService

categoryService = CategoryService()

# name = input('Please type into category name: ')
# description = input('Please type into description: ')
#
# result = categoryService.CreateCategory(name, description)
#
# print(result)

# categoryService.ListCategory()

# Update Business
# 1. İlk önce güncellenecek entity id'sinden yakalanarak kullanıcıya getirilir.
# 2. Kullanıcı bu entity üzerinde değiştirmek istediği alanları değiştirir ve update fonksiyonuna gönderir.
# test => 6300f32a90388cc693302b15

# categoryId = input("Please type into id: ")
# categoryName = input("Please type name: ")
# description = input("Please type description")
#
# result = categoryService.UpdateCategory(categoryId, categoryName, description)
#
# print(result)
#
# print("======================")
#
# categoryService.ListCategory()

categoryService.DeleteCategory("6300f32a90388cc693302b15")

print("======================")

categoryService.ListCategory()

