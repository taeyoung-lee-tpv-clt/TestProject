import os, yaml

environment = os.environ.get("RUN_ENVIRONMENT")
home_direcotry = os.environ.get("PWD")

if environment == None:
    environment = "local"

# Get common setting
config_common = {}
with open(file=f"{home_direcotry}/config/yaml/{environment}/common.yaml", mode="r") as file:
    config_common = yaml.load(stream=file, Loader=yaml.FullLoader)

# Get database setting
config_database = {}
with open(file=f"{home_direcotry}/config/yaml/{environment}/database.yaml", mode="r") as file:
    config_database = yaml.load(stream=file, Loader=yaml.FullLoader)

# Get interface setting(like kafka, apigee...)
config_interface = {}
with open(file=f"{home_direcotry}/config/yaml/{environment}/interface.yaml", mode="r") as file:
    config_interface = yaml.load(stream=file, Loader=yaml.FullLoader)

# Set service account key
if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") == None:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config_common.get("service_account_key")
