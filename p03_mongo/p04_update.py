from connect_mongo import db_test_Z4073

customers_collection = db_test_Z4073["customers_cs"]

print("Update surname to 'Vdaná' for 'Helena Nováková'")
myquery = {"name": "Helena", "surname": "Nováková"}
print(customers_collection.find_one(myquery))
new_value = {"$set": {"surname": "Vdaná"}}
customers_collection.update_one(myquery, new_value)
print(customers_collection.find_one({"name": "Helena"}))

print('-'*80)
print("Add address to customer 'Karel Trojan'")
customers_collection.update_one({"name": "Karel", "surname": "Trojan"},
                                {"$set": {"address": "Vodní 55, Pardubice"}})
print(customers_collection.find_one({"name": "Karel"}))

print('-'*80)
print("Add district to all customers from Ostrava")
myquery = {"address": {"$regex": "Ostrava$"}}
for customer in customers_collection.find(myquery):
    print(customer)
new_value = {"$set": {"district": "Moravskoslezský kraj"}}
response = customers_collection.update_many(myquery, new_value)
print(f"Updated {response.modified_count} records.")
for customer in customers_collection.find(myquery):
    print(customer)
