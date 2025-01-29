import os

import pymongo
from dotenv import load_dotenv

load_dotenv()

# vytvořím klienta
#mongo_client = pymongo.MongoClient("127.0.0.1", 27017)
#mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mongo_client = pymongo.MongoClient(f"mongodb://"
                                   f"{os.getenv("mongo_host", default="127.0.0.1")}:"
                                   f"{os.getenv("mongo_port", default=27017)}")

# vytvoření databáze
db_test_Z4073 = mongo_client.db_test_Z4073
# nebo
db_second_Z4073 = mongo_client["db_second_Z4073"]


if __name__ == '__main__':
    print(f"mongo_client: {mongo_client}")
    print(f"db_test_Z4073: {db_test_Z4073}")
    print(f"db_second_Z4073: {db_second_Z4073}")

    databases = mongo_client.list_database_names()
    print(f"databases: {databases}")

    # vytvoření kolekce ("tabulky")
    customer_collection = db_test_Z4073["customers"]
