import mysql.connector
from pymongo import MongoClient

def mysql_conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="aitutor"
    )

def mongo_conn():
    return MongoClient("mongodb://localhost:27017/")["aitutor"]
