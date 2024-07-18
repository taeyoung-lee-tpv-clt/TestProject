import redis
from common.logging import logger


def redis_server_main():
    logger.info("=======Connection Redis Server=======")
    # Redis 서버에 연결
    client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    # 데이터 삽입
    client.set('key1', 'value1')

    # 데이터 조회
    value = client.get('key1')
    print(f'The value for key1 is: {value}')
