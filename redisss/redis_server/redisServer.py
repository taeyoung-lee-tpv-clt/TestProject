import redis
from common.logging import logger
from pymongo import MongoClient
import pandas as pd
import hashlib
import json
# from namabiru.read_csv import get_df_data

redis_shards = [
    redis.StrictRedis(host='localhost', port=6379, decode_responses=True),
    redis.StrictRedis(host='localhost', port=6381, decode_responses=True)
]

def get_redis_shard(key):
    # 키 해싱을 통해 적절한 Redis 샤드를 선택
    hash_val = int(hashlib.md5(key.encode()).hexdigest(), 16)
    return redis_shards[hash_val % len(redis_shards)]


def redis_server_main(data):
    print("=======Connection Redis Server=======")
    # Redis 서버에 연결
    
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    for key,val in data.items():
        if isinstance(val, pd.Series):
            val = val.to_json()
        shard = get_redis_shard(key)
        # 데이터 삽입
        shard.set(key, val)
        print(val)
        # 데이터 조회
        value = client.get(key)
        print(f'The value for {key} is: {value}')

def mongo_server_main():
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.mydatabase
    collection = db.mycollection