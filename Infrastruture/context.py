
# context modülünde veri tabanı ile iletişime geçmemize yardımcı olacak yapılar oluşturulur.

from pymongo import MongoClient

connectionString = MongoClient('mongodb://localhost:27017')

db = connectionString['yzl_3501']

# region Collections
# projenin kapsamına göre burada ihtiyaç duyulacak colleciton'lar oluşturulur.
categoryCollection = db['category']
# endregion

# region Generate Seed Data
# Proje ilk çalıştırıldığında veri tabanı ile iletişime geçilerek collection oluşturulacak ardın bu collection içerisinde aşağıda oluşturduğumuz sample data insert edilecektir.
# categoryList = [
#     {"name": "Boxing Gloves", "description": "Everlast produce best boxing gloves.", },
#     {"name": "Punching Bags", "description": "Everlast produce best punching bags."},
#     {"name": "Protective Equipment", "description": "Everlast produce best protective equipment."},
# ]
# endregion

# region Insert the Seed Data
# categoryCollection.insert_many(categoryList)
# endregion



