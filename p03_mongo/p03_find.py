from pymongo.errors import OperationFailure

from connect_mongo import db_test_Z4073

customers_collection = db_test_Z4073["customers"]

print("Find one:")
response = customers_collection.find_one()
print(response)

print('-'*80)
print("Find:")
# SELECT * FROM customers;
response = customers_collection.find()
print(response)
for customer in response:
    print(customer)

print('-'*80)
print("Find (only selected attributes/fields)")
# SELECT name, surname FROM customers;
for customer in customers_collection.find({}, {"name": True, "surname": 1}):  # True == 1
    print(customer)

print('-'*80)
print("Find (exclude selected attributes/fields")
for customer in customers_collection.find({}, {"address": False, "email": 0}):  # False == 0
    print(customer)

try:
    print('-'*80)
    print("Find (include and exclude) -> ERROR")
    for customer in customers_collection.find({}, {"name": 1, "surname": 1, "address": 0}):
        print(customer)
except OperationFailure as e:
    print(f"ERROR: {e}")  # nefunguje kombinace 0/1 ve výběru atributů, kromě _id, viz následující příklad

print('-'*80)
print("Find (include name and surname, exclude _id)")
for customer in customers_collection.find({}, {"_id": 0, "name": 1, "surname": 1}):
    print(customer)

print('-'*80)
print("Find customers with surname 'Novák'")
myquery = {"surname": "Novák"}
print(f"Result of query {myquery}:")
for customer in customers_collection.find({"surname": "Novák"}):
    print(customer)
print('-'*40)
for customer in customers_collection.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(customer)

print('-'*80)
print("Find customers with surname > 'N'")
myquery = {"surname": {"$gt": "N"}}  # gt = Greater Then = "Větší než"
print(f"Result of query {myquery}:")
for customer in customers_collection.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(customer)

print('-'*80)
print("Find customers with surname starts with 'N'")
myquery = {"surname": {"$regex": "^N"}}  # gt = Greater Then = "Větší než"
print(f"Result of query {myquery}:")
for customer in customers_collection.find(myquery, {"_id": 0, "name": 1, "surname": 1}):
    print(customer)

print('-'*80)
print("Find customers from Ostrava")
myquery = {"address": {"$regex": "Ostrava$"}}
print(f"Result of query {myquery}:")
for customer in customers_collection.find(myquery, {"_id": 0, "name": 1, "surname": 1, "address": 1}):
    print(customer)

print('-'*80)
print("Find customers from Ostrava with surname 'Nováková'")
myquery = {"surname": "Nováková",  "address": {"$regex": "Ostrava$"}}
print(f"Result of query {myquery}:")
for customer in customers_collection.find(myquery, {"_id": 0, "name": 1, "surname": 1, "address": 1}):
    print(customer)
