"""Exercise 1
Use data in medical-data.json to create a new collection: medicaldata
- Find all rows with procedure_code equal 0F1F4ZC
- Find patient with patient_id equal 74, print his full name
- Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC
"""
import json

from connect_mongo import db_test_Z4073


# Use data in medical-data.json to create a new collection: medicaldata
medicaldata = db_test_Z4073["medicaldata"]

"""
with open('files/medical-data.json') as f:
    data = json.load(f)
    response = medicaldata.insert_many(data)
    print(f"To collection 'medicaldata' were inserted {len(response.inserted_ids)} documents.")
"""

print("Find all rows with procedure_code equal 0F1F4ZC:")
for procedure in medicaldata.find({"procedure_code": "0F1F4ZC"}):
    print(procedure)

print("Find patient with patient_id equal 74, print his full name:")
patient = medicaldata.find_one({"patient_id": 74})
print(f"{patient['first_name']} {patient['last_name']}")

print("Find a procedure performed on 2019-05-24T01:52:37.000Z and update its procedure code to 0F1F4ZC:")
for visit in medicaldata.find({"visit_date.date": "2019-05-24T01:52:37.000Z"}):
    print(visit)

print('-'*40)
response = medicaldata.update_many({"visit_date.date": "2019-05-24T01:52:37.000Z"},
                                   {"$set": {"procedure_code": "0F1F4ZC"}})
for visit in medicaldata.find({"visit_date.date": "2019-05-24T01:52:37.000Z"}):
    print(visit)
