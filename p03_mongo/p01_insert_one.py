from connect_mongo import db_test_Z4073

test_collection = db_test_Z4073["test_collection"]

response = test_collection.insert_one(
    {
        "first_name": "Adam",
        "last_name": "Bernau"
    }
)

print(f"Last inserted id: {response.inserted_id}")
