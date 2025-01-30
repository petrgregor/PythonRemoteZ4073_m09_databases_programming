from pymongo.errors import OperationFailure

from connect_mongo import db_test_Z4073, mongo_client

customers_collection = db_test_Z4073["customers"]

for customer in customers_collection.find():
    print(customer)

try:
    with mongo_client.start_session() as session:
        with session.start_transaction():
            response = customers_collection.insert_one(
                {"_id": 9, "name": "Matouš"}, session=session
            )
            print(f"Last inserted id: {response.inserted_id}")
            response = customers_collection.insert_one(
                {"_id": 1, "name": "Norbert"}, session=session
            )
            print(f"Last inserted id: {response.inserted_id}")
except OperationFailure as e:
    print(f"ERROR: {e}")


print("END")
