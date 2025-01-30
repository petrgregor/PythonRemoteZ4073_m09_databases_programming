from connect_mongo import db_test_Z4073

customers_collection = db_test_Z4073["customers_cs"]

print("Delete one customer 'Lubomír Sobota'")
myquery = {"name": "Lubomír", "surname": "Sobota"}
for customer in customers_collection.find(myquery):
    print(customer)
#customers_collection.delete_one(myquery)
print('-'*40)
for customer in customers_collection.find(myquery):
    print(customer)

print('-'*80)
print("Delete customers from 'Praha'")
myquery = {"address": {"$regex": "Praha$"}}
for customer in customers_collection.find(myquery):
    print(customer)
response = customers_collection.delete_many(myquery)
print(f"Deleted {response.deleted_count} records.")
for customer in customers_collection.find(myquery):
    print(customer)

print('-'*80)
print("Delete all customers")
response = customers_collection.delete_many({})
print(f"Deleted {response.deleted_count} records.")

print('-'*80)
print("Delete collection")
customers_collection.drop()
