from concurrent import futures
from common.logging import logger
from ConceptAcpt.redis_server.redisServer import redis_server_main

def serve():
    redis_server_main()

if __name__ == "__main__":
    logger.info("Redis Server Start!")
    serve()
