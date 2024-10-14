import os

class Config:
    SECRET_KEY = 'Secret_Key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://server2:T3t0npack@192.168.1.28/school18?charset=utf8mb4&collation=utf8mb4_general_ci'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    Debug = True