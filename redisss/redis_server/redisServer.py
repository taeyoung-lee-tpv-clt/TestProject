import redis
from common.logging import logger
from pymongo import MongoClient
import pandas as pd
# from namabiru.read_csv import get_df_data

def redis_server_main(data):
    print("=======Connection Redis Server=======")
    # Redis 서버에 연결
    
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    for key,val in data.items():
        if isinstance(val, pd.Series):
            val = val.to_json()

        # 데이터 삽입
        client.set(key, val)
        print(val)
        # 데이터 조회
        value = client.get(key)
        print(f'The value for {key} is: {value}')

def mongo_server_main():
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.mydatabase
    collection = db.mycollection