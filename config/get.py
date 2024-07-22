import os, yaml

environment = os.environ.get("RUN_ENVIRONMENT")
home_direcotry = os.environ.get("PWD")

if environment == None:
    environment = "local"

# Get common setting
config_common = {}
with open(file=f"{home_direcotry}/config/yaml/{environment}/common.yaml", mode="r") as file:
    config_common = yaml.load(stream=file, Loader=yaml.FullLoader)



#############################REDIS##############################

# YAML 파일 로드
with open('redis_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Redis 설정 파일 생성
with open('redis.conf', 'w') as file:
    file.write(f"port {config['server']['port']}\n")
    file.write(f"bind {config['server']['bind']}\n")
    file.write(f"maxclients {config['server']['maxclients']}\n")
    file.write(f"databases {config['server']['databases']}\n\n")

    file.write(f"dbfilename {config['persistence']['dbfilename']}\n")
    file.write(f"dir {config['persistence']['dir']}\n")
    file.write(f"appendonly {config['persistence']['appendonly']}\n")
    file.write(f"appendfilename {config['persistence']['appendfilename']}\n")
    file.write(f"appendfsync {config['persistence']['appendfsync']}\n")
    for save in config['persistence']['save']:
        file.write(f"save {save['interval']} {save['changes']}\n")
    file.write("\n")

    file.write(f"loglevel {config['logging']['loglevel']}\n")
    file.write(f"logfile {config['logging']['logfile']}\n\n")

    file.write(f"maxmemory {config['memory']['maxmemory']}\n")
    file.write(f"maxmemory-policy {config['memory']['maxmemory-policy']}\n\n")

    # Uncomment and adjust the following lines if replication settings are needed
    # file.write(f"replicaof {config['replication']['replicaof']}\n")
    # file.write(f"masterauth {config['replication']['masterauth']}\n\n")

    file.write(f"requirepass {config['security']['requirepass']}\n\n")

    file.write(f"cluster-enabled {config['cluster']['enabled']}\n")
    file.write(f"cluster-config-file {config['cluster']['config-file']}\n")
    file.write(f"cluster-node-timeout {config['cluster']['node-timeout']}\n\n")

    file.write(f"timeout {config['connections']['timeout']}\n")
    file.write(f"tcp-keepalive {config['connections']['tcp-keepalive']}\n\n")

    file.write(f"lua-time-limit {config['lua']['time-limit']}\n\n")

    file.write(f"daemonize {config['daemon']['daemonize']}\n")
    file.write(f"supervised {config['daemon']['supervised']}\n\n")

    file.write(f"hash-max-ziplist-entries {config['optimization']['hash-max-ziplist-entries']}\n")
    file.write(f"hash-max-ziplist-value {config['optimization']['hash-max-ziplist-value']}\n")
    file.write(f"list-max-ziplist-size {config['optimization']['list-max-ziplist-size']}\n")
    file.write(f"zset-max-ziplist-entries {config['optimization']['zset-max-ziplist-entries']}\n")
    file.write(f"zset-max-ziplist-value {config['optimization']['zset-max-ziplist-value']}\n")
